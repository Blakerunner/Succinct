from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import requests

from resources.language_types import LanguageTypes

SENTENCES_COUNT = 10
LANGUAGE = "english"


def get_text_from_url(url: str) -> list:
    """
    Return summarized text from the url.

    :param url: a string
    :return: list of strings
    :raise KeyError: if language is not supported
    """
    request = requests.head(url)
    language = LanguageTypes[request.headers["Content-language"].replace("-", "_").upper()]
    parser = HtmlParser.from_url(url, Tokenizer(language))
    return get_summary_from_parser(parser, language)


def get_text_from_file(file_name: str) -> list:
    """
    Return summarized text from the text file.

    :param file_name: a str, language: string
    :return: list of strings
    """
    parser = PlaintextParser.from_file(file_name, Tokenizer(LANGUAGE))
    return get_summary_from_parser(parser, LANGUAGE)


def get_text_from_word():
    pass


def get_text_from_pdf():
    pass


def get_text_from_txt():
    pass


def get_text_from_str(text: str) -> list:
    """
    Return summarized text from the text string.

    :param text: a string
    :return: list of strings
    """
    parser = PlaintextParser.from_string(text, Tokenizer(LANGUAGE))
    return get_summary_from_parser(parser, LANGUAGE)


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
    return summarizer(parser.document, SENTENCES_COUNT)
