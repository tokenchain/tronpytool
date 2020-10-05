# !/usr/bin/env python
# coding: utf-8

# !/usr/bin/env python
# coding: utf-8
import logging

from tronpytool import Tron

private = "444e82ce44f09f7wfwfwefwfwef2ba804388ab12db9d"
logger = logging.getLogger()

tron = Tron().setNetwork('nile')
tron.private_key = private
tron.getKey().printKeys()
