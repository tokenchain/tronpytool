#!/usr/bin/env python
# coding: utf-8
from tronpytool import Tron
from tronpytool import HttpProvider

tron = Tron().setNetwork('nile')

result = tron.trx.get_transaction('TxId')
