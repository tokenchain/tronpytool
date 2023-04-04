#!/usr/bin/env python
# --------------------------------------------------------------------
# Copyright (c) fInvention.c. All rights reserved.
# Licensed under the MIT License.
# See License.txt in the project root for license information.
# --------------------------------------------------------------------

import sys

import pkg_resources
from eth_account import Account  # noqa: E402

from .constants import Evm, Bolors
from .compile.paths import Paths
from .compile.service import Service, BackgroundRun
from .main import Tron  # noqa: E402
from .tronbrew import TronBrew
from .pen.collectfundscn import Collector
from .pen.contracttest import CoreSimulatePlayers
from .pen.eventtest import EventTestCase
from .pen.membertest import MemberNetworkTestCase
from .providers.gracefulinterrupter import GracefulInterruptHandler
from .providers.http import HttpProvider  # noqa: E402


if sys.version_info < (3, 5):
    raise EnvironmentError("Python 3.5 or above is required")

__version__ = pkg_resources.get_distribution("tronpytool").version

__all__ = [
    '__version__',
    'HttpProvider',
    'Account',
    'CoreSimulatePlayers',
    'MemberNetworkTestCase',
    'Tron',
    'Collector',
    'EventTestCase',
    'Service',
    'GracefulInterruptHandler',
    'BackgroundRun',
    'Paths',
    'Evm',
    'Bolors',
    'TronBrew'
]
