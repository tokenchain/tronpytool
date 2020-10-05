# !/usr/bin/env python
# coding: utf-8

# !/usr/bin/env python
# coding: utf-8
import logging

from tronpytool import Tron

private = "444e82ce44f09f701e0b09f5773a0cc6823bf100b4e83552ba804388ab12db9d"
logger = logging.getLogger()

tron = Tron().setNetwork('nile')
tron.private_key = private
account = tron.generate_address(tron.get_private_key())

logger.debug('Generated account: ')
logger.debug('- Private Key: ' + account.private_key)
logger.debug('- Public Key: ' + account.public_key)
logger.debug('- Address: ')
logger.debug('-- Base58: ' + account.address.base58)
logger.debug('-- Hex: ' + account.address.hex)
logger.debug('-----------')
