import datetime
import unittest

import requests


class MultipleInstanceException(Exception):
    pass


class Bank:  # singleton
    GET = "http://www.cbr.ru/scripts/XML_daily.asp?date_req={day}/{month}/{year}"

    __OBJ = None

    def __init__(self):
        if Bank.__OBJ is not None:
            raise MultipleInstanceException
        Bank.__OBJ = self

    @property
    def exchange_rates(self):
        today = datetime.date.today()
        day = f"0{today.day}" if today.day < 10 else today.day
        month = f"0{today.month}" if today.month < 10 else today.month
        year = today.year

        url = Bank.GET.format(day=day, month=month, year=year)
        resp = requests.get(url)

        return resp.text


class BankTest(unittest.TestCase):
    def test_response(self):
        resp = Bank().exchange_rates
        self.assertRegex(resp, r"\<\?xml")

    def test_singleton(self):
        Bank()
        self.assertRaises(MultipleInstanceException, Bank)
