#!/usr/bin/env python
# coding: utf-8
import os

from key import private_key, wallet_address
from tronpygen.gen_py.masonic_coal import MasonicCoal
from tronpytool.compile.basetest import CoreDeploy, WrapContract

# import sys
# the mock-0.3.1 dir contains testcase.py, testutils.py & mock.py
# sys.path.append('/Users/hesdx/Documents/piplines/tron-tool-py/tronpytool')
NETWORK = "nile"
ROOT = os.path.join(os.path.dirname(__file__))


class WrapDeploy(CoreDeploy):
    """Deploy wrap contract in the deployment"""

    def __init__(self):
        _workSpace = WrapContract(NETWORK).setMasterKey(wallet_address, private_key)
        _tron = _workSpace.getClientTron()
        super().__init__(_tron)

    def connect_deploy(self, sol: bool, deploy: bool) -> "WrapDeploy":
        self.connect_deploy_core(ROOT, sol, deploy)
        return self

    def deploy_BonusKeep(self):
        if self.is_deployment():
            print("=== Deploy contract with this settings {}".format("BonusKeep"))
            self.deploy(self.sol_cont, "BonusKeep")

    def deploy_MasonicCoal(self):
        if self.is_deployment():
            long_params = []
            print("=== Deploy args lprovider parameters {}".format(long_params))
            self.deploy(self.sol_cont, "MasonicCoal")

    def init_test_query(self):
        collection2 = self.tron.trx.get_contract(self.getAddr("MasonicCoal"))
        print('Transaction: ')
        print(collection2)
        print('-----------')
        collection1 = self.tron.trx.get_contract(self.getAddr("BonusKeep"))
        print('Transaction: ')
        print(collection1)
        print('-----------')

    def after_deployment_initialize_settings(self):
        self.complete_deployment()
        self.preview_all_addresses()

        contract = MasonicCoal(self.tron, self.getAddr("MasonicCoal"))
        (testing,) = contract.is_blueprint()
        print("=== 📶 is testing mode {}:".format(testing))
        # (settime,) = contract.what_time()
        # timeex = datetime.fromtimestamp(settime)
        # print("=== 📶 the contract time is now {}:".format(timeex))
        contract.set_keeper(self.getAddr("BonusKeep"))
        #contract.get_user_by_address(self.getAddr("BonusKeep"), 0)

        return self
