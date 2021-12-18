from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from langdetect import detect
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import requests
import nltk
from PyPDF2 import PdfFileReader
import docx2txt

nltk.download('punkt')

SENTENCES_COUNT = 10
LANGUAGE = "english"


def get_text_from_url(url: str) -> list:
    """
    Return summarized text from the url.

    :param url: a string
    :return: list of strings
    """
    request = requests.head(url)
    language = request.headers["Content-language"]
    try:
        parser = HtmlParser.from_url(url, Tokenizer(language))
        return get_summary_from_parser(parser, language)
    except LookupError:
        print("Language not supported")


def get_text_from_file(file_name: str) -> list:
    """
    Return summarized text from the text file.

    :param file_name: a str, language: string
    :return: list of strings
    """
    if file_name[file_name.rfind('.') + 1:] == "pdf":
        return get_text_from_pdf(file_name)
    elif file_name[file_name.rfind('.') + 1:] == "docx":
        return get_text_from_word(file_name)
    else:
        return get_text_from_txt(file_name)


def get_text_from_txt(file_name:str) -> list:
    """
    Return summarized version from a text file.
    :param file_name: str
    :return: list of strings
    """
    with open(file_name, "r", encoding="utf-8") as f:
        data = f.read()
        return get_text_from_str(data)


def get_text_from_word(file_name: str) -> list:
    """
    Return summarized version from a docx file.
    :param file_name: str
    :return: list of strings
    """
    doc = docx2txt.process(file_name)
    return get_text_from_str(doc)


def get_text_from_pdf(file_name: str) -> list:
    """
    Return summarized version from a pdf file.
    :param file_name: str
    :return: list of strings
    """
    pdf = PdfFileReader(file_name)
    pdf_str = "\n".join([pdf.getPage(page).extractText() for page in range(pdf.numPages)])
    return get_text_from_str(pdf_str)


def get_text_from_str(text: str) -> list:
    """
    Return summarized text from the text string.
    :param text: a string
    :return: list of strings
    """
    language = detect(text)
    if language in ('zh-cn', 'zh-tw'):
        language = 'zh'
    try:
        parser = PlaintextParser.from_string(text, Tokenizer(language))
        return get_summary_from_parser(parser, language)
    except LookupError:
        print("Language not supported")


def get_summary_from_parser(parser: PlaintextParser, language: str):
    """
    Return summary from parsed response.
    :param parser: a PlainTextParser object
    :param language: a string
    :return: a list of strings
    """
    stemmer = Stemmer(language)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(language)
    return [str(sentence) for sentence in summarizer(parser.document, SENTENCES_COUNT)]


