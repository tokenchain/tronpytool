# !/usr/bin/env python
# coding: utf-8
import codecs
import json
import os
import subprocess
import time

from tronpytool import Tron

ROOT = os.path.join(os.path.dirname(__file__))


class SolcWrap(object):
    """docstring for SolcWrap"""
    OUTPUT_BUILD = "build"
    WORKSPACE_PATH = ""
    solfolder = ""
    file_name = "xxx.sol"
    prefixname = ""
    statement = 'End : {}, IO File {}'

    def __init__(self, workspace):
        """param workspace: this is the local path for the file set"""
        self.WORKSPACE_PATH = workspace
        super(SolcWrap, self).__init__()

    def SetOutput(self, path):
        self.OUTPUTBUILD = path
        return self

    def SetSolPath(self, path):
        self.solfolder = path
        return self

    def BuildRemote(self):
        """This is the remote command to execute the solc_remote bash file
        using remote compile method to compile the sol files
        all works will be done with the remote server or using the docker"""
        list_files = subprocess.run(["{}/solc_remote".format(self.WORKSPACE_PATH)])
        print("The exit code was: %d" % list_files.returncode)
        return self

    def WrapModel(self):
        """setup initialize the file for combined.json"""
        pathc = os.path.join(self.WORKSPACE_PATH, self.OUTPUT_BUILD, "combined.json")
        try:
            pathcli = codecs.open(pathc, 'r', 'utf-8-sig')
            self.combined_data = json.load(pathcli)
        except Exception as e:
            print("Problems from loading items from the file: ", e)
        return self

    def GetCodeClass(self, classname) -> [any, any]:
        p1bin = os.path.join(self.WORKSPACE_PATH, self.OUTPUT_BUILD, "{}.bin".format(classname))
        p2abi = os.path.join(self.WORKSPACE_PATH, self.OUTPUT_BUILD, "{}.abi".format(classname))
        bin = codecs.open(p1bin, 'r', 'utf-8-sig').read()
        abi = json.load(codecs.open(p2abi, 'r', 'utf-8-sig'))
        return abi, bin

    def byClassName(self, path, classname):
        return "{prefix}:{name}".format(prefix=path, name=classname)

    def GetCodeTag(self, fullname):
        return self.combined_data["contracts"][fullname]["abi"], self.combined_data["contracts"][fullname]["bin"]

    def GetCode(self, path, classname) -> [str, str]:
        abi = self.combined_data["contracts"][self.byClassName(path, classname)]["abi"]
        bin = self.combined_data["contracts"][self.byClassName(path, classname)]["bin"]
        return abi, bin

    def writeFile(self, content, filename):
        fo = open(filename, "w")
        fo.write(content)
        fo.close()
        print(self.statement.format(time.ctime(), filename))

    @property
    def workspace(self):
        return self.WORKSPACE_PATH

    def StoreTxResult(self, tx_result_data, filepath):
        self.writeFile(json.dumps(tx_result_data, ensure_ascii=False), filepath)


class CoreDeploy:
    """DEFI Contract deployment
    with the right strategies
    """
    _contract_dict: dict
    FILE_CONTRACT = "backedup"
    ACTION_FOLDER = "deploy_results"
    COLLECTION_CONTRACTS = "deployments"

    def __init__(self, tron: Tron):
        self.tron = tron
        self._contract_dict = dict()

    @property
    def backupname(self) -> str:
        """preview the file name"""
        return self.FILE_CONTRACT

    @backupname.setter
    def backupname(self, filename: str) -> None:
        """the file name does not require extension name"""
        self.FILE_CONTRACT = filename

    @property
    def deployment_location(self) -> str:
        return self.COLLECTION_CONTRACTS

    @deployment_location.setter
    def deployment_location(self, path: str) -> None:
        self.COLLECTION_CONTRACTS = path

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

    def preview_all_addresses(self) -> None:
        print(self._contract_dict)

    def deployedAddrsFilePath(self) -> str:
        return os.path.join(self.sol_cont.workspace, self.ACTION_FOLDER,
                            "{}.json".format(self.COLLECTION_CONTRACTS))

    def is_deployment(self) -> bool:
        return self.is_deploy

    def connect_deploy_core(self, workspace: str, rebuild=False, deploy=False) -> None:
        if rebuild:
            sol_contr = SolcWrap(workspace).BuildRemote()
        else:
            sol_contr = SolcWrap(workspace)

        self.is_deploy = deploy
        self.sol_cont = sol_contr
        if not deploy:
            """try to load up the file from the existing path"""
            try:
                self._contract_dict = json.load(codecs.open(self.deployedAddrsFilePath(), 'r', 'utf-8-sig'))
                print("==== 🛄 data is prepared and it is ready now.. ")
                self.preview_all_addresses()
            except ValueError:
                pass
            except TypeError as e:
                print(e)

    def complete_deployment(self) -> None:
        """store up the deployed contrcat addresses to the local file storage"""
        self.sol_cont.StoreTxResult(self._contract_dict, self.deployedAddrsFilePath())

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
        self.sol_cont.WrapModel()
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


class WrapContract(object):
    """docstring for WrapContract The contract for this BOBA TEA"""

    def __init__(self, _network):
        nn1 = Tron().setNetwork(_network)
        if nn1.is_connected():
            self.tron_client = nn1
        else:
            print(
                "client v1 is not connected. please check the internet connection or the service is down! network: {}".format(
                    _network))

        self._tron_module = nn1.trx
        self._contract = None

    def getClientTron(self) -> "Tron":
        return self.tron_client

    def setMasterKey(self, pub: str, pri: str) -> "WrapContract":
        self.tron_client.private_key = pri
        self.tron_client.default_address = pub
        return self

    def initContract(self, contract_metadata) -> "WrapContract":
        """
        Load and initiate contract interface by using the deployed contract json metadata
        try:
        except FileNotFoundError as e:
            print("Could not load the file ", e)
        except Exception as e:
            print("Problems from loading items from the file: ", e)
        """
        contractDict = json.load(codecs.open(contract_metadata, 'r', 'utf-8-sig'))
        trn = contractDict["transaction"]
        hex_address = trn["contract_address"]
        self.transction_detail = contractDict
        self.trc_address = self.tron_client.address.from_hex(hex_address)
        print("@contract address {} from hex {}".format(self.trc_address, hex_address))
        # self.init_internal_contract()
        self.implcontract()
        return self

    def getTxID(self):
        return self.transction_detail["txid"]

    def implcontract(self):
        pass