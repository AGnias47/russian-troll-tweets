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
