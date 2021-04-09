#!/usr/bin/env python
# coding: utf-8
import os

from examples.codec.core.lib import WrapDeploy
from tronpytool import __version__

print(__version__)
caddress = "TGzXbPmnnRyknJbvx7BCJqpdg76uiZaE92"

ROOT = os.path.join(os.path.dirname(__file__))
# original owner address
NETWORK = "nile"


class BulkManager:
    def __init__(self, dat, tron):
        self.datlist = dat
        self.tron = tron

    def getSENDAddresses(self) -> list:
        list_address = list()
        for c in self.datlist:
            list_address.append(c[0])
        return list_address

    def getSENDAmountBalances(self) -> list:
        list_address = list()
        for c in self.datlist:
            list_address.append(c[1])

        return list_address

    def getSENDTotal(self) -> int:
        total = 0
        for c in self.datlist:
            total += int(c[1])
        return total


test_data = [
    ["TPbUCNXm4qe2a8yN34SJ7L1rTo1v8dFQsw", 1000000],
    ["TN8oagb1NUMWNDHZrsCsdyMmAawDe4CynM", 1000000],
    ["TJ1Ed3UGC6iLrKJrfdmBVdNypeRP7CTA6i", 1000000],
    ["THwiDYo5iuNZGfEe8mResy6rU878ec7nG2", 1000000],
    ["TPvfywKCHP4AZXJhgXbwmgprN48qwXLfmT", 1000000],
]

if __name__ == '__main__':
    ws = WrapDeploy(ROOT, NETWORK)
    ws.connect(ROOT, False)
    ws.preMulti()
    sendOb = BulkManager(test_data, ws.tron)
    print("total {}".format(sendOb.getSENDTotal()))
    # print("address {}".format(sendOb.getSENDAddresses()))

    ws.getContactBS().bulk_send_trx(
        sendOb.getSENDAddresses(),
        sendOb.getSENDAmountBalances(),
        sendOb.getSENDTotal()
    )
