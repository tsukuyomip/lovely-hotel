# coding: utf-8

import re

from dataexception import DataException


class Checker:
    def __is_include_upper_character(self, s):
        if re.search("[A-Z]+", s) is None:
            return False
        return True
