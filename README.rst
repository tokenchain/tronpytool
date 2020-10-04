===================
TRON API for Python
===================

A Python API for interacting with the Tron (TRX)

.. image:: https://img.shields.io/pypi/v/tronpytool.svg
    :target: https://pypi.python.org/pypi/tronpytool

.. image:: https://img.shields.io/pypi/pyversions/tronpytool.svg
    :target: https://pypi.python.org/pypi/tronpytool

.. image:: https://api.travis-ci.com/iexbase/tron-api-python.svg?branch=master
    :target: https://travis-ci.com/iexbase/tron-api-python
    
.. image:: https://img.shields.io/github/issues/iexbase/tron-api-python.svg
    :target: https://github.com/iexbase/tron-api-python/issues
    
.. image:: https://img.shields.io/github/issues-pr/iexbase/tron-api-python.svg
    :target: https://github.com/iexbase/tron-api-python/pulls

.. image:: https://api.codacy.com/project/badge/Grade/8a5ae1e1cc834869b1094ea3b0d24f78
   :alt: Codacy Badge
   :target: https://app.codacy.com/app/serderovsh/tron-api-python?utm_source=github.com&utm_medium=referral&utm_content=iexbase/tron-api-python&utm_campaign=Badge_Grade_Dashboard
    

------------

**A Command-Line Interface framework**

You can install it in a system-wide location via pip:

.. code-block:: bash

    sudo pip3 install tronpytool

Or install it locally using `virtualenv <https://github.com/pypa/virtualenv>`__:

.. code-block:: bash

    virtualenv -p /usr/bin/python3 ~/tronpytool
    source ~/tronpytool/bin/activate
    pip3 install tronpytool

------------

Usage
=====
Specify the API endpoints:


Smart Contract
--------------

.. code-block:: python

    from tronpytool import HttpProvider
    from tronpytool import Tron

    full_node = HttpProvider('https://api.trongrid.io')
    solidity_node = HttpProvider('https://api.trongrid.io')
    event_server = HttpProvider('https://api.trongrid.io')

    # option 1
    tron = Tron(full_node=full_node,
                solidity_node=solidity_node,
                event_server=event_server)

    # option 2
    tron_v2 = Tron()

    # option 3
    tron_v3 = Tron(
        default_address='TRWBqiqoFZysoAeyR1J35ibuyc8EvhUAoY',
        private_key='...'
    )

    # option 4
    tron_v4 = Tron().setNetwork('nile')

..

Base Example
------------

.. code-block:: python
    
    from tronpytool import Tron
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
    logger = logging.getLogger()

    tron = Tron().setNetwork("nile")

    account = tron.create_account()
    is_valid = bool(tron.trx.is_address(account.address.hex))

    logger.debug('Generated account: ')
    logger.debug('- Private Key: ' + account.private_key)
    logger.debug('- Public Key: ' + account.public_key)
    logger.debug('- Address: ')
    logger.debug('-- Base58: ' + account.address.base58)
    logger.debug('-- Hex: ' + account.address.hex)
    logger.debug('-- isValid: ' + str(is_valid))
    logger.debug('-----------')
    
    transaction = tron.trx.get_transaction('757a14cef293c69b1cf9b9d3d19c2e40a330c640b05c6ffa4d54609a9628758c')

    logger.debug('Transaction: ')
    logger.debug('- Hash: ' + transaction['txID'])
    logger.debug('- Transaction: ' + json.dumps(transaction, indent=2))
    logger.debug('-----------')
    
    # Events
    event_result = tron.trx.get_event_result('TGEJj8eus46QMHPgWQe1FJ2ymBXRm96fn1', 0, 'Notify')

    logger.debug('Event result:')
    logger.debug('Contract Address: TGEJj8eus46QMHPgWQe1FJ2ymBXRm96fn1')
    logger.debug('Event Name: Notify')
    logger.debug('Block Number: 32162')
    logger.debug('- Events: ' + json.dumps(event_result, indent=2))

More samples and snippets are available at `examples <https://github.com/iexbase/tron-api-python/tree/master/examples>`__.

Documentation
=============

Documentation is available at `docs <https://tronpytool-for-python.readthedocs.io/en/latest/>`__.


Donations
=============

TRON: TRWBqiqoFZysoAeyR1J35ibuyc8EvhUAoY

