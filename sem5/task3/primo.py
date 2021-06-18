import abc
import datetime
import unittest

import requests


class Bank:  # abstract
    GET = "http://www.cbr.ru/scripts/XML_daily.asp?date_req={day}/{month}/{year}"
    OBJ = None  # singleton

    def __init__(self):
        pass

    @property
    @abc.abstractmethod
    def exchange_rates(self) -> str:
        pass

    @classmethod
    def create(cls) -> 'Bank':
        if cls.OBJ is None:
            cls.OBJ = cls()
        return cls.OBJ


class XmlBank(Bank):
    OBJ = None  # singleton

    @property
    def exchange_rates(self) -> str:
        today = datetime.date.today()
        day = f"0{today.day}" if today.day < 10 else today.day
        month = f"0{today.month}" if today.month < 10 else today.month
        year = today.year

        url = XmlBank.GET.format(day=day, month=month, year=year)
        resp = requests.get(url)

        return resp.text


class BankTest(unittest.TestCase):
    def setUp(self) -> None:
        XmlBank.OBJ = None

    def test_response(self):
        resp = XmlBank().exchange_rates
        self.assertRegex(resp, r"\<\?xml")

    def test_singleton(self):
        b1 = XmlBank.create()
        b2 = XmlBank.create()
        self.assertIs(b1, b2)
