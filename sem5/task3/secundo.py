import json
import xmltodict

from sem5.task3.primo import XmlBank, Bank


class JsonBank(XmlBank):
    OBJ = None  # singleton

    def __init__(self):
        super().__init__()
        self._bank = None  # type: 'Bank' or None

    @property
    def bank(self) -> 'Bank':
        return self._bank

    @bank.setter
    def bank(self, bank):
        self._bank = bank

    @property
    def exchange_rates(self) -> str:
        xml = self._bank.exchange_rates

        o = xmltodict.parse(xml)

        return json.dumps(o)


xml_bank = XmlBank.create()

json_bank = JsonBank.create()
json_bank.bank = xml_bank

json_string = json_bank.exchange_rates
with open("./rates.json", "wt") as file:
    file.write(json_string)
