from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

import json

from sumy.parsers.html import HtmlParser
from langdetect import detect
from models.db import db
from models.user import User
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from flask import session
import requests
import nltk
from PyPDF2 import PdfFileReader
import docx2txt

nltk.download('punkt')

SENTENCES_COUNT = 10
LANGUAGE = "english"


def get_text_from_url(url: str, summary_length: int = 10) -> list:
    """
    Return summarized text from the url.
    :param summary_length: length of the summary in lines.
    :param url: a string
    :return: list of strings
    """
    request = requests.head(url)
    language = request.headers["Content-language"]
    try:
        parser = HtmlParser.from_url(url, Tokenizer(language))
        update_user(url=url)
        return get_summary_from_parser(parser, language, summary_length)
    except LookupError:
        print("Language not supported")


def get_text_from_file(file_name: str, summary_length: int = 10) -> list:
    """
    Return summarized text from the text file.
    :param summary_length: length of the summary in lines.
    :param file_name: a str, language: string
    :return: list of strings
    """
    if file_name[file_name.rfind('.') + 1:] == "pdf":
        return get_text_from_pdf(file_name, summary_length)
    elif file_name[file_name.rfind('.') + 1:] == "docx":
        return get_text_from_word(file_name, summary_length)
    else:
        return get_text_from_txt(file_name, summary_length)


def get_text_from_txt(file_name: str, summary_length: int = 10) -> list:
    """
    Return summarized version from a text file.
    :param summary_length: length of the summary in lines.
    :param file_name: str
    :return: list of strings
    """
    with open(file_name, "r", encoding="utf-8") as f:
        data = f.read()
        return get_text_from_str(data, summary_length)


def get_text_from_word(file_name: str, summary_length: int = 10) -> list:
    """
    Return summarized version from a docx file.
    :param summary_length: length of the summary in lines.
    :param file_name: str
    :return: list of strings
    """
    doc = docx2txt.process(file_name)
    return get_text_from_str(doc, summary_length)


def get_text_from_pdf(file_name: str, summary_length: int = 10) -> list:
    """
    Return summarized version from a pdf file.
    :param summary_length: length of the summary in lines.
    :param file_name: str
    :return: list of strings
    """
    pdf = PdfFileReader(file_name)
    pdf_str = "\n".join([pdf.getPage(page).extractText() for page in range(pdf.numPages)])
    return get_text_from_str(pdf_str, summary_length)


def update_user_text(user, text, curr_text):
    if curr_text:
        user.queries = json.dumps([text] + json.loads(curr_text))
        db.session.commit()
    else:
        user.queries = json.dumps([text])
        db.session.commit()


def update_user(text=None, url=None):
    if not (text or url):
        return

    user_id = session.get("user_id")
    user = User.query.filter_by(id=user_id).first()
    curr_text = user.queries
    update_user_text(user, text, curr_text)


def get_text_from_str(text: str, summary_length:int = 10) -> list:
    """
    Return summarized text from the text string.
    :param summary_length: length of the summary in lines.
    :param text: a string
    :return: list of strings
    """
    language = detect(text)
    if language in ('zh-cn', 'zh-tw'):
        language = 'zh'
    try:
        parser = PlaintextParser.from_string(text, Tokenizer(language))
        update_user(text=text)
        return get_summary_from_parser(parser, language, summary_length)
    except LookupError:
        print("Language not supported")


def get_summary_from_parser(parser: PlaintextParser, language: str, summary_length: int = 10):
    """
    Return summary from parsed response.
    :param summary_length: length of the summary in lines.
    :param parser: a PlainTextParser object
    :param language: a string
    :return: a list of strings
    """
    stemmer = Stemmer(language)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(language)
    return [str(sentence) for sentence in summarizer(parser.document, summary_length)]
