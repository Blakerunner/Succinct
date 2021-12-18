from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from googletrans import Translator

from language_types import LanguageTypes

SENTENCES_COUNT = 10


def get_text_from_url(url: str, language: str) -> list:
    """
    Return summarized text from the url.

    :param language:
    :param url: a string
    :return: list of strings
    """
    parser = HtmlParser.from_url(url, Tokenizer(language))
    return get_summary_from_parser(parser)


def get_text_from_file(file_name: str, language: str) -> list:
    """
    Return summarized text from the text file.

    :param language:
    :param file_name: a string
    :return: list of strings
    """
    parser = PlaintextParser.from_file(file_name, Tokenizer(language))
    return get_summary_from_parser(parser)


def get_text_from_word():
    pass


def get_text_from_pdf():
    pass


def get_text_from_txt():
    pass


def get_text_from_str(text: str, language: str) -> list:
    """
    Return summarized text from the text string.

    :param language:
    :param text: a string
    :return: list of strings
    """
    parser = PlaintextParser.from_string(text, Tokenizer(language))
    return get_summary_from_parser(parser)


def get_summary_from_parser(parser: PlaintextParser):
    """
    Return summary from parsed response.

    :param parser: a PlainTextParser object
    :return: a list of strings
    """

    translator = Translator()
    detected_language = translator.detect(parser.document.sentences[0])
    language = LanguageTypes(str(detected_language.lan).capitalize().replace("-", "_"))

    stemmer = Stemmer(language)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(language)
    return summarizer(parser.document, SENTENCES_COUNT)


if __name__ == '__main__':
    essay = "essay, an analytic, interpretative, or critical literary composition usually much shorter and less systematic and formal than a dissertation or thesis and usually dealing with its subject from a limited and often personal point of view. " \
            "Some early treatises—such as those of Cicero on the pleasantness of old age or on the art of “divination,” Seneca on anger or clemency, and Plutarch on the passing of oracles—presage to a certain degree the form and tone of the essay, but not until the late 16th century was the flexible and deliberately nonchalant and versatile form of the essay perfected by the French writer Michel de Montaigne. Choosing the name essai to emphasize that his compositions were attempts or endeavours, a groping toward the expression of his personal thoughts and experiences, Montaigne used the essay as a means of self-discovery. His Essais, published in their final form in 1588, are still considered among the finest of their kind. Later writers who most nearly recall the charm of Montaigne include, in England, Robert Burton, though his whimsicality is more erudite, Sir Thomas Browne, and Laurence Sterne, and in France, with more self-consciousness and pose, André Gide and Jean Cocteau." \
            "At the beginning of the 17th century, social manners, the cultivation of politeness, and the training of an accomplished gentleman became the theme of many essayists. This theme was first exploited by the Italian Baldassare Castiglione in his Il libro del cortegiano (1528; The Book of the Courtier). The influence of the essay and of genres allied to it, such as maxims, portraits, and sketches, proved second to none in molding the behavior of the cultured classes, first in Italy, then in France, and, through French influence, in most of Europe in the 17th century. Among those who pursued this theme was the 17th-century Spanish Jesuit Baltasar Gracián in his essays on the art of worldly wisdom." \
            "Keener political awareness in the 18th century, the age of Enlightenment, made the essay an all-important vehicle for the criticism of society and religion. Because of its flexibility, its brevity, and its potential both for ambiguity and for allusions to current events and conditions, it was an ideal tool for philosophical reformers. The Federalist Papers in America and the tracts of the French Revolutionaries are among the countless examples of attempts during this period to improve the human condition through the essay." \
            "The genre also became the favoured tool of traditionalists of the 18th and 19th centuries, such as Edmund Burke and Samuel Taylor Coleridge, who looked to the short, provocative essay as the most potent means of educating the masses. Essays such as Paul Elmer More’s long series of Shelburne Essays (published between 1904 and 1935), T.S. Eliot’s After Strange Gods (1934) and Notes Towards the Definition of Culture (1948), and others that attempted to reinterpret and redefine culture, established the genre as the most fitting to express the genteel tradition at odds with the democracy of the new world." \
            "Whereas in several countries the essay became the chosen vehicle of literary and social criticism, in other countries the genre became semipolitical, earnestly nationalistic, and often polemical, playful, or bitter. Essayists such as Robert Louis Stevenson and Willa Cather wrote with grace on several lighter subjects, and many writers—including Virginia Woolf, Edmund Wilson, and Charles du Bos—mastered the essay as a form of literary criticism."
    a = get_text_from_str(essay, "english")
    print(a)
