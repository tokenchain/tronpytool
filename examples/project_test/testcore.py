import os

from tronpytool import Tron
from tronpytool.compile.basetest import SolcWrap

ROOT = os.path.join(os.path.dirname(__file__))


class CoreDeploy:
    """DEFI Contract deployment
    with the right strategies
    """
    _contract_dict: dict
    ACTION_FOLDER = "deploy_results"

    def __init__(self, tron: Tron):
        self.tron = tron
        self._contract_dict = dict()

    def getAddr(self, keyname: str) -> str:
        """example: TT67rPNwgmpeimvHUMVzFfKsjL9GZ1wGw8"""
        return self._contract_dict.get(keyname)

    def getAddr0x(self, keyname: str) -> str:
        """example: 0xBBC8C05F1B09839E72DB044A6AA57E2A5D414A10"""
        return self.tron.address.to_hex_0x(self._contract_dict.get(keyname))

    def getAddr0x41(self, keyname: str) -> str:
        """example: 0x41BBC8C05F1B09839E72DB044A6AA57E2A5D414A10"""
        return self.tron.address.to_hex_0x_41(self._contract_dict.get(keyname))

    def getAddrHex(self, keyname: str) -> str:
        """example: 41BBC8C05F1B09839E72DB044A6AA57E2A5D414A10"""
        return self.tron.address.to_hex(self._contract_dict.get(keyname))

    def getAllAddress(self) -> dict:
        return self._contract_dict

    def preview_all_addresses(self):
        print(self._contract_dict)

    def connect_deploy(self, rebuild=False, deploy=False) -> "CoreDeploy":
        if rebuild:
            sol_contr = SolcWrap(ROOT).BuildRemote()
        else:
            sol_contr = SolcWrap(ROOT)

        self.is_deploy = deploy
        self.sol_cont = sol_contr
        return self

    def deploy(self, sol_wrap: SolcWrap, classname: str, params: list = []) -> str:
        """This is using the faster way to deploy files by using the specific abi and bin files"""
        _abi, _bytecode = sol_wrap.GetCodeClass(classname)
        contractwork = self.tron.trx.contract(abi=_abi, bytecode=_bytecode)
        contract = contractwork.constructor()
        tx_data = contract.transact(
            fee_limit=10 ** 9,
            call_value=0,
            parameters=params,
            consume_user_resource_percent=1)
        print("======== TX Result ✅")
        sign = self.tron.trx.sign(tx_data)
        print("======== Signing {} ✅".format(classname))
        result = self.tron.trx.broadcast(sign)
        path = "{}/{}.json".format(self.ACTION_FOLDER, classname)
        print("======== Broadcast Result ✅ -> {}".format(path))
        sol_wrap.StoreTxResult(result, path)
        contract_address = self.tron.address.from_hex(result["transaction"]["contract_address"])
        self._contract_dict[classname] = contract_address
        print("======== address saved to ✅ {} -> {}".format(contract_address, classname))
        return contract_address

    def classic_deploy(self, sol_wrap: SolcWrap, path: str, classname: str, params: list = []) -> str:
        """This is the older method of deployment reading the only combined.json file"""
        _abi, _bytecode = sol_wrap.GetCode(path, classname)
        contractwork = self.tron.trx.contract(abi=_abi, bytecode=_bytecode)
        contract = contractwork.constructor()
        tx_data = contract.transact(
            fee_limit=10 ** 9,
            call_value=0,
            parameters=params,
            consume_user_resource_percent=1)
        print("======== TX Result ✅")
        sign = self.tron.trx.sign(tx_data)
        print("======== Signing {} ✅".format(classname))
        result = self.tron.trx.broadcast(sign)
        path = "{}/{}.json".format(self.ACTION_FOLDER, classname)
        print("======== Broadcast Result ✅ -> {}".format(path))
        sol_wrap.StoreTxResult(result, path)
        contract_address = self.tron.address.from_hex(result["transaction"]["contract_address"])
        self._contract_dict[classname] = contract_address
        print("======== address saved to ✅ {} -> {}".format(contract_address, classname))
        return contract_address
