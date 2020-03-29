#!/usr/bin/env python3
#
#   A. Gnias
#
#   Linux 5.3.0-40-generic #32-Ubuntu
#   Python 3.7.5
#   Vim 8.1


import csv


def read_csv_as_list_of_dicts(filepath):
    data = list()
    with open(filepath, "r") as f:
        raw = csv.DictReader(f, delimiter=",")
        for row in raw:
            data.append(row)
    return data


def clean_words_list(words):
    words = [word.lower() for word in words]
    common_words = {
        "",
        "-",
        "~",
        "&amp;",
        "a",
        "an",
        "the",
        "on",
        "to",
        "is",
        "for",
        "and",
        "of",
        "you",
        "in",
        "that",
        "should",
        "be",
        "from",
        "when",
        "have",
        "has",
        "was",
        "with",
        "at",
        "are",
        "this",
        "by",
        "it",
        "i",
        "my",
        "not",
        "your",
        "as",
        "will",
        "about",
        "all",
        "who",
        "they",
        "after",
        "we",
        "are",
        "his",
        "out",
        "but",
        "up",
        "our",
        "like",
        ":",
        "\|",
        "people",
        "he",
        "just",
        "new",
        "me",
        "get",
        "can",
        "more",
        "so",
        "what",
        "i'm",
        "do",
        "if",
        "or",
        "via",
        "their",
        "&",
        "don't",
        "no",
        "one",
        "over",
        "how",
        "us",
        "it's",
    }
    words = list(filter(lambda x: x not in common_words, words))
    # Need to account for words linked to punctuation
    return words
