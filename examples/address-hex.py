#!/usr/bin/env python
# coding: utf-8
from tronpytool import Tron
from tronpytool import HttpProvider

tron = Tron().setNetwork('nile')


tron.address.to_hex('TT67rPNwgmpeimvHUMVzFfKsjL9GZ1wGw8')
# result: 41BBC8C05F1B09839E72DB044A6AA57E2A5D414A10

tron.address.from_hex('41BBC8C05F1B09839E72DB044A6AA57E2A5D414A10')
# result: TT67rPNwgmpeimvHUMVzFfKsjL9GZ1wGw8
