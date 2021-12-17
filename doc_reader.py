from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer


# def get_text_from_file(file_name: str) -> list:
#     """
#     Return summarized text from the text file.
#
#     :param file_name: a string
#     :return: list of strings
#     """
#     parser = PlaintextParser.from_file(file_name, Tokenizer(LANGUAGE))
#     return get_summary_from_parser(parser)
#
#
# def get_text_from_word():
#     pass
#
#
# def get_text_from_pdf():
#     pass