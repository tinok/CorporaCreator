from urllib.parse import unquote
from html.parser import HTMLParser


class _HTMLStripper(HTMLParser):
    """Class that strips HTML from strings.

    Examples:
        >>> stripper = _HTMLStripper()
        >>> stripper.feed(html)
        >>> nohtml = stripper.get_data()
    """

    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return "".join(self.fed)


def _strip_tags(html):
    """Removes HTML tags from passed text.

    Args:
      html (str): String containing HTML

    Returns:
      (str): String with HTML removed
    """
    s = _HTMLStripper()
    s.feed(html)
    return s.get_data()


def common(sentence):
    """Cleans up the passed sentence in a language independent manner, removing or reformatting invalid data.

    Args:
      sentence (str): Sentence to be cleaned up.

    Returns:
      (str): Cleaned up sentence. Returning None or a `str` of whitespace flags the sentence as invalid.
    """

    # Decode any URL encoded elements of sentence
    sentence = unquote(sentence)
    # Remove any HTML tags
    sentence = _strip_tags(sentence)
    # TODO: Clean up data in a language independent manner
    return sentence
