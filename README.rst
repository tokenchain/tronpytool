======================================
TRON API for Python The only Library
======================================

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





Code compile
------------

Integration of forge that can work perfectly with latest version with ONE LINE code.

.. code-block:: python

    # !/usr/bin/env python
    # coding: utf-8
    import os

    from tronpytool import TronBrew, Evm

    solidity_files = [
        "vault/token/RaceToken.sol",
    ]

    ROOT = '.../Documents/b95/devtron'
    FACTORY = '$HOME/Documents/piplines/factoryabi'

    print("-----> job from here")
    print(ROOT)
    print("-----> now its ready to go")

    TronBrew(ROOT, FACTORY).setClassSolNames(solidity_files).setEvm(Evm.ISTANBUL).useForge().localTranspile()




Documentation
=============
Read the library manual by the `manual <docs/tronpytool/index.html>`__
Documentation is available at `docs <https://tronpytool-for-python.readthedocs.io/en/latest/>`__.


Donations
=============