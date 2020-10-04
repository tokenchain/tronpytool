#!/usr/bin/env python
# coding: utf-8
from attrdict import AttrDict

from tronpytool import Tron
from tronpytool.constants import handle_res

tron = Tron().setNetwork('nile')
private_key = '444e82ce44f09f701e0b09f5773a0cc6823bf100b4e83552ba804388ab12db9d'
wallet_address = 'TR3TEXGWZvY5DZryrQx6bkmCK6whBr7SE4'
contract='TRXut9s5NKLtXYw8Fj7ze4jUuHyLuHkYxw'
tron.private_key = private_key
tron.default_address = wallet_address

data = {'contract_address': 'TRXut9s5NKLtXYw8Fj7ze4jUuHyLuHkYxw', 'function_selector': 'name()',
        'issuer_address': AttrDict({'hex': '41A5576E55542477CE999F2D3A8C242697B0FCF416',
                                    'base58': 'TR3TEXGWZvY5DZryrQx6bkmCK6whBr7SE4'}), 'fee_limit': 30000,
        'call_value': 0,
        'token_value': 0, 'token_id': 0, 'parameters': []}

collection = tron.trx.get_contract(contract)
print('Transaction: ')
print(collection)
print('-----------')


get_name_tx = tron.transaction_builder.trigger_smart_contract(data)

ok, key, message = tron.transaction_builder.handle_ret(get_name_tx)

if ok:
    print("=======debug request result {}".format(key))
    print(get_name_tx)
    print(message)
    print("=======end event report ========")
else:
    raise KeyError('Request returns Error - {} msg:{} txt:{}'.format(key, message, ""))
