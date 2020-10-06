#!/usr/bin/env python
# coding: utf-8

"""Generated wrapper for MasonicCoal Solidity contract."""

# pylint: disable=too-many-arguments

import json
from typing import (  # pylint: disable=unused-import
    List,
    Tuple,
    Union,
)

from hexbytes import HexBytes
from tronpytool import Tron
from tronpytool.common.datastructures import AttributeDict
from tronpytool.compile.basecore import ContractMethod, Validator
from tronpytool.contract import ContractFunction, Contract

# Try to import a custom validator class definition; if there isn't one,
# declare one that we can instantiate for the default argument to the
# constructor for MasonicCoal below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        MasonicCoalValidator,
    )
except ImportError:

    class MasonicCoalValidator(  # type: ignore
        Validator
    ):
        """No-op input validator."""

try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class AccountExTransactionMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the accountExTransaction method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction, validator: Validator = None):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, seller_account: str, buyer_account: str):
        """Validate the inputs to the accountExTransaction method."""
        self.validator.assert_valid(
            method_name='accountExTransaction',
            parameter_name='seller_account',
            argument_value=seller_account,
        )
        seller_account = self.validate_and_checksum_address(seller_account)
        self.validator.assert_valid(
            method_name='accountExTransaction',
            parameter_name='buyer_account',
            argument_value=buyer_account,
        )
        buyer_account = self.validate_and_checksum_address(buyer_account)
        return (seller_account, buyer_account)

    def call(self, seller_account: str, buyer_account: str, tx_params=None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (seller_account, buyer_account) = self.validate_and_normalize_inputs(seller_account, buyer_account)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(seller_account, buyer_account).call(tx_params)

    def send_transaction(self, seller_account: str, buyer_account: str, tx_params=None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (seller_account, buyer_account) = self.validate_and_normalize_inputs(seller_account, buyer_account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(seller_account, buyer_account).transact(tx_params.as_dict())

    def build_transaction(self, seller_account: str, buyer_account: str, tx_params=None) -> dict:
        """Construct calldata to be used as input to the method."""
        (seller_account, buyer_account) = self.validate_and_normalize_inputs(seller_account, buyer_account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(seller_account, buyer_account).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, seller_account: str, buyer_account: str, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        (seller_account, buyer_account) = self.validate_and_normalize_inputs(seller_account, buyer_account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(seller_account, buyer_account).estimateGas(tx_params.as_dict())


class AccountSalesMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the accountSales method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction, validator: Validator = None):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, sales_amount: int):
        """Validate the inputs to the accountSales method."""
        self.validator.assert_valid(
            method_name='accountSales',
            parameter_name='sales_amount',
            argument_value=sales_amount,
        )
        # safeguard against fractional inputs
        sales_amount = int(sales_amount)
        return (sales_amount)

    def call(self, sales_amount: int, tx_params=None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (sales_amount) = self.validate_and_normalize_inputs(sales_amount)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(sales_amount).call(tx_params)

    def send_transaction(self, sales_amount: int, tx_params=None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (sales_amount) = self.validate_and_normalize_inputs(sales_amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(sales_amount).transact(tx_params.as_dict())

    def build_transaction(self, sales_amount: int, tx_params=None) -> dict:
        """Construct calldata to be used as input to the method."""
        (sales_amount) = self.validate_and_normalize_inputs(sales_amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(sales_amount).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, sales_amount: int, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        (sales_amount) = self.validate_and_normalize_inputs(sales_amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(sales_amount).estimateGas(tx_params.as_dict())


class AddWhitelistAdminMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the addWhitelistAdmin method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction, validator: Validator = None):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, account: str):
        """Validate the inputs to the addWhitelistAdmin method."""
        self.validator.assert_valid(
            method_name='addWhitelistAdmin',
            parameter_name='account',
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        return (account)

    def call(self, account: str, tx_params=None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(account).call(tx_params)

    def send_transaction(self, account: str, tx_params=None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).transact(tx_params.as_dict())

    def build_transaction(self, account: str, tx_params=None) -> dict:
        """Construct calldata to be used as input to the method."""
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, account: str, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).estimateGas(tx_params.as_dict())


class BangMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the bang method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction, validator: Validator = None):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, time: int):
        """Validate the inputs to the bang method."""
        self.validator.assert_valid(
            method_name='bang',
            parameter_name='time',
            argument_value=time,
        )
        # safeguard against fractional inputs
        time = int(time)
        return (time)

    def call(self, time: int, tx_params=None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (time) = self.validate_and_normalize_inputs(time)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(time).call(tx_params)

    def send_transaction(self, time: int, tx_params=None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (time) = self.validate_and_normalize_inputs(time)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(time).transact(tx_params.as_dict())

    def build_transaction(self, time: int, tx_params=None) -> dict:
        """Construct calldata to be used as input to the method."""
        (time) = self.validate_and_normalize_inputs(time)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(time).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, time: int, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        (time) = self.validate_and_normalize_inputs(time)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(time).estimateGas(tx_params.as_dict())


class CanGoToVegasMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the canGoToVegas method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params=None) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params)
        return bool(returned)

    def estimate_gas(self, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class CapReachedMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the capReached method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction, validator: Validator = None):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, che: str):
        """Validate the inputs to the capReached method."""
        self.validator.assert_valid(
            method_name='capReached',
            parameter_name='che',
            argument_value=che,
        )
        che = self.validate_and_checksum_address(che)
        return (che)

    def call(self, che: str, tx_params=None) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (che) = self.validate_and_normalize_inputs(che)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(che).call(tx_params)
        return bool(returned)

    def estimate_gas(self, che: str, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        (che) = self.validate_and_normalize_inputs(che)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(che).estimateGas(tx_params.as_dict())


class CompareStrMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the compareStr method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction, validator: Validator = None):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, src: str, src_compared: str):
        """Validate the inputs to the compareStr method."""
        self.validator.assert_valid(
            method_name='compareStr',
            parameter_name='src',
            argument_value=src,
        )
        self.validator.assert_valid(
            method_name='compareStr',
            parameter_name='src_compared',
            argument_value=src_compared,
        )
        return (src, src_compared)

    def call(self, src: str, src_compared: str, tx_params=None) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (src, src_compared) = self.validate_and_normalize_inputs(src, src_compared)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(src, src_compared).call(tx_params)
        return bool(returned)

    def estimate_gas(self, src: str, src_compared: str, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        (src, src_compared) = self.validate_and_normalize_inputs(src, src_compared)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(src, src_compared).estimateGas(tx_params.as_dict())


class ConfirmInviteCodeMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the confirmInviteCode method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction, validator: Validator = None):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, code: str):
        """Validate the inputs to the confirmInviteCode method."""
        self.validator.assert_valid(
            method_name='confirmInviteCode',
            parameter_name='code',
            argument_value=code,
        )
        return (code)

    def call(self, code: str, tx_params=None) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (code) = self.validate_and_normalize_inputs(code)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(code).call(tx_params)
        return bool(returned)

    def estimate_gas(self, code: str, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        (code) = self.validate_and_normalize_inputs(code)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(code).estimateGas(tx_params.as_dict())


class ContractExistsMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the contractExists method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction, validator: Validator = None):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, contractc: str):
        """Validate the inputs to the contractExists method."""
        self.validator.assert_valid(
            method_name='contractExists',
            parameter_name='contractc',
            argument_value=contractc,
        )
        contractc = self.validate_and_checksum_address(contractc)
        return (contractc)

    def call(self, contractc: str, tx_params=None) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (contractc) = self.validate_and_normalize_inputs(contractc)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(contractc).call(tx_params)
        return bool(returned)

    def estimate_gas(self, contractc: str, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        (contractc) = self.validate_and_normalize_inputs(contractc)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(contractc).estimateGas(tx_params.as_dict())


class ContractInvalidateMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the contractInvalidate method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params=None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method().call(tx_params)

    def send_transaction(self, tx_params=None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params=None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class CreditKeyMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the creditKey method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction, validator: Validator = None):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, member: str):
        """Validate the inputs to the creditKey method."""
        self.validator.assert_valid(
            method_name='creditKey',
            parameter_name='member',
            argument_value=member,
        )
        member = self.validate_and_checksum_address(member)
        return (member)

    def call(self, member: str, tx_params=None) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (member) = self.validate_and_normalize_inputs(member)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(member).call(tx_params)
        return bool(returned)

    def send_transaction(self, member: str, tx_params=None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (member) = self.validate_and_normalize_inputs(member)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(member).transact(tx_params.as_dict())

    def build_transaction(self, member: str, tx_params=None) -> dict:
        """Construct calldata to be used as input to the method."""
        (member) = self.validate_and_normalize_inputs(member)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(member).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, member: str, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        (member) = self.validate_and_normalize_inputs(member)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(member).estimateGas(tx_params.as_dict())


class DistributeDiamondsMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the distribute_diamonds method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction, validator: Validator = None):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, balance: int):
        """Validate the inputs to the distribute_diamonds method."""
        self.validator.assert_valid(
            method_name='distribute_diamonds',
            parameter_name='balance',
            argument_value=balance,
        )
        # safeguard against fractional inputs
        balance = int(balance)
        return (balance)

    def call(self, balance: int, tx_params=None) -> Tuple[int, int, int]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (balance) = self.validate_and_normalize_inputs(balance)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(balance).call(tx_params)
        return (returned[0], returned[1], returned[2],)

    def estimate_gas(self, balance: int, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        (balance) = self.validate_and_normalize_inputs(balance)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(balance).estimateGas(tx_params.as_dict())


class ElectionMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the election method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params=None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params)
        return str(returned)

    def estimate_gas(self, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class EndRoundMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the endRound method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params=None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method().call(tx_params)

    def send_transaction(self, tx_params=None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params=None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class EndTestMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the endTest method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params=None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method().call(tx_params)

    def send_transaction(self, tx_params=None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params=None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class FaucetMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the faucet method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction, validator: Validator = None):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, start: int, end: int):
        """Validate the inputs to the faucet method."""
        self.validator.assert_valid(
            method_name='faucet',
            parameter_name='start',
            argument_value=start,
        )
        # safeguard against fractional inputs
        start = int(start)
        self.validator.assert_valid(
            method_name='faucet',
            parameter_name='end',
            argument_value=end,
        )
        # safeguard against fractional inputs
        end = int(end)
        return (start, end)

    def call(self, start: int, end: int, tx_params=None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (start, end) = self.validate_and_normalize_inputs(start, end)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(start, end).call(tx_params)

    def send_transaction(self, start: int, end: int, tx_params=None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (start, end) = self.validate_and_normalize_inputs(start, end)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(start, end).transact(tx_params.as_dict())

    def build_transaction(self, start: int, end: int, tx_params=None) -> dict:
        """Construct calldata to be used as input to the method."""
        (start, end) = self.validate_and_normalize_inputs(start, end)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(start, end).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, start: int, end: int, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        (start, end) = self.validate_and_normalize_inputs(start, end)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(start, end).estimateGas(tx_params.as_dict())


class ForceCapMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the forceCap method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction, validator: Validator = None):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, v: int):
        """Validate the inputs to the forceCap method."""
        self.validator.assert_valid(
            method_name='forceCap',
            parameter_name='v',
            argument_value=v,
        )
        # safeguard against fractional inputs
        v = int(v)
        return (v)

    def call(self, v: int, tx_params=None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (v) = self.validate_and_normalize_inputs(v)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(v).call(tx_params)

    def send_transaction(self, v: int, tx_params=None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (v) = self.validate_and_normalize_inputs(v)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(v).transact(tx_params.as_dict())

    def build_transaction(self, v: int, tx_params=None) -> dict:
        """Construct calldata to be used as input to the method."""
        (v) = self.validate_and_normalize_inputs(v)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(v).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, v: int, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        (v) = self.validate_and_normalize_inputs(v)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(v).estimateGas(tx_params.as_dict())


class ForceFerrariMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the forceFerrari method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction, validator: Validator = None):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, k: int):
        """Validate the inputs to the forceFerrari method."""
        self.validator.assert_valid(
            method_name='forceFerrari',
            parameter_name='k',
            argument_value=k,
        )
        # safeguard against fractional inputs
        k = int(k)
        return (k)

    def call(self, k: int, tx_params=None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (k) = self.validate_and_normalize_inputs(k)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(k).call(tx_params)

    def send_transaction(self, k: int, tx_params=None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (k) = self.validate_and_normalize_inputs(k)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(k).transact(tx_params.as_dict())

    def build_transaction(self, k: int, tx_params=None) -> dict:
        """Construct calldata to be used as input to the method."""
        (k) = self.validate_and_normalize_inputs(k)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(k).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, k: int, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        (k) = self.validate_and_normalize_inputs(k)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(k).estimateGas(tx_params.as_dict())


class FwmodeMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the fwmode method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params=None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method().call(tx_params)

    def send_transaction(self, tx_params=None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params=None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class GenerationMulbyLvMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the generationMulbyLv method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction, validator: Validator = None):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, level: int, times: int):
        """Validate the inputs to the generationMulbyLv method."""
        self.validator.assert_valid(
            method_name='generationMulbyLv',
            parameter_name='level',
            argument_value=level,
        )
        # safeguard against fractional inputs
        level = int(level)
        self.validator.assert_valid(
            method_name='generationMulbyLv',
            parameter_name='times',
            argument_value=times,
        )
        # safeguard against fractional inputs
        times = int(times)
        return (level, times)

    def call(self, level: int, times: int, tx_params=None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (level, times) = self.validate_and_normalize_inputs(level, times)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(level, times).call(tx_params)
        return int(returned)

    def estimate_gas(self, level: int, times: int, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        (level, times) = self.validate_and_normalize_inputs(level, times)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(level, times).estimateGas(tx_params.as_dict())


class GetEmcMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getEmc method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction, validator: Validator = None):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, value: int):
        """Validate the inputs to the getEmc method."""
        self.validator.assert_valid(
            method_name='getEmc',
            parameter_name='value',
            argument_value=value,
        )
        # safeguard against fractional inputs
        value = int(value)
        return (value)

    def call(self, value: int, tx_params=None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (value) = self.validate_and_normalize_inputs(value)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(value).call(tx_params)
        return int(returned)

    def estimate_gas(self, value: int, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        (value) = self.validate_and_normalize_inputs(value)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(value).estimateGas(tx_params.as_dict())


class GetLevelMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getLevel method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction, validator: Validator = None):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, value: int):
        """Validate the inputs to the getLevel method."""
        self.validator.assert_valid(
            method_name='getLevel',
            parameter_name='value',
            argument_value=value,
        )
        # safeguard against fractional inputs
        value = int(value)
        return (value)

    def call(self, value: int, tx_params=None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (value) = self.validate_and_normalize_inputs(value)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(value).call(tx_params)
        return int(returned)

    def estimate_gas(self, value: int, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        (value) = self.validate_and_normalize_inputs(value)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(value).estimateGas(tx_params.as_dict())


class GetLineUserIdMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getLineUserId method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction, validator: Validator = None):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, index: int, rou_id: int):
        """Validate the inputs to the getLineUserId method."""
        self.validator.assert_valid(
            method_name='getLineUserId',
            parameter_name='index',
            argument_value=index,
        )
        # safeguard against fractional inputs
        index = int(index)
        self.validator.assert_valid(
            method_name='getLineUserId',
            parameter_name='rouId',
            argument_value=rou_id,
        )
        # safeguard against fractional inputs
        rou_id = int(rou_id)
        return (index, rou_id)

    def call(self, index: int, rou_id: int, tx_params=None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (index, rou_id) = self.validate_and_normalize_inputs(index, rou_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index, rou_id).call(tx_params)
        return int(returned)

    def estimate_gas(self, index: int, rou_id: int, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        (index, rou_id) = self.validate_and_normalize_inputs(index, rou_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index, rou_id).estimateGas(tx_params.as_dict())


class GetNodeLevelMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getNodeLevel method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction, validator: Validator = None):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, value: int):
        """Validate the inputs to the getNodeLevel method."""
        self.validator.assert_valid(
            method_name='getNodeLevel',
            parameter_name='value',
            argument_value=value,
        )
        # safeguard against fractional inputs
        value = int(value)
        return (value)

    def call(self, value: int, tx_params=None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (value) = self.validate_and_normalize_inputs(value)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(value).call(tx_params)
        return int(returned)

    def estimate_gas(self, value: int, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        (value) = self.validate_and_normalize_inputs(value)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(value).estimateGas(tx_params.as_dict())


class GetUserAddressByCodeMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getUserAddressByCode method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction, validator: Validator = None):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, code: str):
        """Validate the inputs to the getUserAddressByCode method."""
        self.validator.assert_valid(
            method_name='getUserAddressByCode',
            parameter_name='code',
            argument_value=code,
        )
        return (code)

    def call(self, code: str, tx_params=None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (code) = self.validate_and_normalize_inputs(code)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(code).call(tx_params)
        return str(returned)

    def estimate_gas(self, code: str, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        (code) = self.validate_and_normalize_inputs(code)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(code).estimateGas(tx_params.as_dict())


class GetUserAddressByIdMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getUserAddressById method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction, validator: Validator = None):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, _id: int):
        """Validate the inputs to the getUserAddressById method."""
        self.validator.assert_valid(
            method_name='getUserAddressById',
            parameter_name='id',
            argument_value=_id,
        )
        # safeguard against fractional inputs
        _id = int(_id)
        return (_id)

    def call(self, _id: int, tx_params=None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(_id).call(tx_params)
        return str(returned)

    def estimate_gas(self, _id: int, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        (_id) = self.validate_and_normalize_inputs(_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_id).estimateGas(tx_params.as_dict())


class GetUserByAddressMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getUserByAddress method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction, validator: Validator = None):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, member: str, round_id: int):
        """Validate the inputs to the getUserByAddress method."""
        self.validator.assert_valid(
            method_name='getUserByAddress',
            parameter_name='member',
            argument_value=member,
        )
        member = self.validate_and_checksum_address(member)
        self.validator.assert_valid(
            method_name='getUserByAddress',
            parameter_name='roundId',
            argument_value=round_id,
        )
        # safeguard against fractional inputs
        round_id = int(round_id)
        return (member, round_id)

    def call(self, member: str, round_id: int, tx_params=None) -> Tuple[List[int], str, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (member, round_id) = self.validate_and_normalize_inputs(member, round_id)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(member, round_id).call(tx_params)
        return (returned[0], returned[1], returned[2],)

    def estimate_gas(self, member: str, round_id: int, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        (member, round_id) = self.validate_and_normalize_inputs(member, round_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(member, round_id).estimateGas(tx_params.as_dict())


class GinzaMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the ginza method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction, validator: Validator = None):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, addr: str, status: int):
        """Validate the inputs to the ginza method."""
        self.validator.assert_valid(
            method_name='ginza',
            parameter_name='addr',
            argument_value=addr,
        )
        addr = self.validate_and_checksum_address(addr)
        self.validator.assert_valid(
            method_name='ginza',
            parameter_name='status',
            argument_value=status,
        )
        # safeguard against fractional inputs
        status = int(status)
        return (addr, status)

    def call(self, addr: str, status: int, tx_params=None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (addr, status) = self.validate_and_normalize_inputs(addr, status)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(addr, status).call(tx_params)

    def send_transaction(self, addr: str, status: int, tx_params=None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (addr, status) = self.validate_and_normalize_inputs(addr, status)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(addr, status).transact(tx_params.as_dict())

    def build_transaction(self, addr: str, status: int, tx_params=None) -> dict:
        """Construct calldata to be used as input to the method."""
        (addr, status) = self.validate_and_normalize_inputs(addr, status)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(addr, status).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, addr: str, status: int, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        (addr, status) = self.validate_and_normalize_inputs(addr, status)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(addr, status).estimateGas(tx_params.as_dict())


class ImportMemberMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the importMember method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction, validator: Validator = None):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, addr: str, invite_code: str, de_vici_code: str):
        """Validate the inputs to the importMember method."""
        self.validator.assert_valid(
            method_name='importMember',
            parameter_name='addr',
            argument_value=addr,
        )
        addr = self.validate_and_checksum_address(addr)
        self.validator.assert_valid(
            method_name='importMember',
            parameter_name='inviteCode',
            argument_value=invite_code,
        )
        self.validator.assert_valid(
            method_name='importMember',
            parameter_name='deViciCode',
            argument_value=de_vici_code,
        )
        return (addr, invite_code, de_vici_code)

    def call(self, addr: str, invite_code: str, de_vici_code: str, tx_params=None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (addr, invite_code, de_vici_code) = self.validate_and_normalize_inputs(addr, invite_code, de_vici_code)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(addr, invite_code, de_vici_code).call(tx_params)

    def send_transaction(self, addr: str, invite_code: str, de_vici_code: str, tx_params=None) -> Union[
        HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (addr, invite_code, de_vici_code) = self.validate_and_normalize_inputs(addr, invite_code, de_vici_code)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(addr, invite_code, de_vici_code).transact(tx_params.as_dict())

    def build_transaction(self, addr: str, invite_code: str, de_vici_code: str, tx_params=None) -> dict:
        """Construct calldata to be used as input to the method."""
        (addr, invite_code, de_vici_code) = self.validate_and_normalize_inputs(addr, invite_code, de_vici_code)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(addr, invite_code, de_vici_code).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, addr: str, invite_code: str, de_vici_code: str, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        (addr, invite_code, de_vici_code) = self.validate_and_normalize_inputs(addr, invite_code, de_vici_code)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(addr, invite_code, de_vici_code).estimateGas(tx_params.as_dict())


class InputRewardByLvMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the inputRewardByLv method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction, validator: Validator = None):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, level: int):
        """Validate the inputs to the inputRewardByLv method."""
        self.validator.assert_valid(
            method_name='inputRewardByLv',
            parameter_name='level',
            argument_value=level,
        )
        # safeguard against fractional inputs
        level = int(level)
        return (level)

    def call(self, level: int, tx_params=None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (level) = self.validate_and_normalize_inputs(level)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(level).call(tx_params)
        return int(returned)

    def estimate_gas(self, level: int, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        (level) = self.validate_and_normalize_inputs(level)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(level).estimateGas(tx_params.as_dict())


class IsBlueprintMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the isBlueprint method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params=None) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params)
        return bool(returned)

    def estimate_gas(self, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class IsOwnerMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the isOwner method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params=None) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params)
        return bool(returned)

    def estimate_gas(self, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class IsWhitelistAdminMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the isWhitelistAdmin method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction, validator: Validator = None):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, account: str):
        """Validate the inputs to the isWhitelistAdmin method."""
        self.validator.assert_valid(
            method_name='isWhitelistAdmin',
            parameter_name='account',
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        return (account)

    def call(self, account: str, tx_params=None) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(account).call(tx_params)
        return bool(returned)

    def estimate_gas(self, account: str, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).estimateGas(tx_params.as_dict())


class LinedepositMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the linedeposit method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction, validator: Validator = None):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, start: int, end: int):
        """Validate the inputs to the linedeposit method."""
        self.validator.assert_valid(
            method_name='linedeposit',
            parameter_name='start',
            argument_value=start,
        )
        # safeguard against fractional inputs
        start = int(start)
        self.validator.assert_valid(
            method_name='linedeposit',
            parameter_name='end',
            argument_value=end,
        )
        # safeguard against fractional inputs
        end = int(end)
        return (start, end)

    def call(self, start: int, end: int, tx_params=None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (start, end) = self.validate_and_normalize_inputs(start, end)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(start, end).call(tx_params)

    def send_transaction(self, start: int, end: int, tx_params=None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (start, end) = self.validate_and_normalize_inputs(start, end)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(start, end).transact(tx_params.as_dict())

    def build_transaction(self, start: int, end: int, tx_params=None) -> dict:
        """Construct calldata to be used as input to the method."""
        (start, end) = self.validate_and_normalize_inputs(start, end)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(start, end).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, start: int, end: int, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        (start, end) = self.validate_and_normalize_inputs(start, end)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(start, end).estimateGas(tx_params.as_dict())


class NagoyaMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the nagoya method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction, validator: Validator = None):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, line: int):
        """Validate the inputs to the nagoya method."""
        self.validator.assert_valid(
            method_name='nagoya',
            parameter_name='line',
            argument_value=line,
        )
        # safeguard against fractional inputs
        line = int(line)
        return (line)

    def call(self, line: int, tx_params=None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (line) = self.validate_and_normalize_inputs(line)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(line).call(tx_params)

    def send_transaction(self, line: int, tx_params=None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (line) = self.validate_and_normalize_inputs(line)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(line).transact(tx_params.as_dict())

    def build_transaction(self, line: int, tx_params=None) -> dict:
        """Construct calldata to be used as input to the method."""
        (line) = self.validate_and_normalize_inputs(line)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(line).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, line: int, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        (line) = self.validate_and_normalize_inputs(line)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(line).estimateGas(tx_params.as_dict())


class NodeRewardbyLvMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the nodeRewardbyLv method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction, validator: Validator = None):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, level: int):
        """Validate the inputs to the nodeRewardbyLv method."""
        self.validator.assert_valid(
            method_name='nodeRewardbyLv',
            parameter_name='level',
            argument_value=level,
        )
        # safeguard against fractional inputs
        level = int(level)
        return (level)

    def call(self, level: int, tx_params=None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (level) = self.validate_and_normalize_inputs(level)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(level).call(tx_params)
        return int(returned)

    def estimate_gas(self, level: int, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        (level) = self.validate_and_normalize_inputs(level)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(level).estimateGas(tx_params.as_dict())


class OwnerMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the owner method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params=None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params)
        return str(returned)

    def estimate_gas(self, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class ReleaseDiamondsMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the releaseDiamonds method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction, validator: Validator = None):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, m1: str, m2: str, luck_members: List[str]):
        """Validate the inputs to the releaseDiamonds method."""
        self.validator.assert_valid(
            method_name='releaseDiamonds',
            parameter_name='m1',
            argument_value=m1,
        )
        m1 = self.validate_and_checksum_address(m1)
        self.validator.assert_valid(
            method_name='releaseDiamonds',
            parameter_name='m2',
            argument_value=m2,
        )
        m2 = self.validate_and_checksum_address(m2)
        self.validator.assert_valid(
            method_name='releaseDiamonds',
            parameter_name='luck_members',
            argument_value=luck_members,
        )
        return (m1, m2, luck_members)

    def call(self, m1: str, m2: str, luck_members: List[str], tx_params=None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (m1, m2, luck_members) = self.validate_and_normalize_inputs(m1, m2, luck_members)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(m1, m2, luck_members).call(tx_params)

    def send_transaction(self, m1: str, m2: str, luck_members: List[str], tx_params=None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (m1, m2, luck_members) = self.validate_and_normalize_inputs(m1, m2, luck_members)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(m1, m2, luck_members).transact(tx_params.as_dict())

    def build_transaction(self, m1: str, m2: str, luck_members: List[str], tx_params=None) -> dict:
        """Construct calldata to be used as input to the method."""
        (m1, m2, luck_members) = self.validate_and_normalize_inputs(m1, m2, luck_members)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(m1, m2, luck_members).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, m1: str, m2: str, luck_members: List[str], tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        (m1, m2, luck_members) = self.validate_and_normalize_inputs(m1, m2, luck_members)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(m1, m2, luck_members).estimateGas(tx_params.as_dict())


class RemoveWhitelistAdminMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the removeWhitelistAdmin method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction, validator: Validator = None):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, account: str):
        """Validate the inputs to the removeWhitelistAdmin method."""
        self.validator.assert_valid(
            method_name='removeWhitelistAdmin',
            parameter_name='account',
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        return (account)

    def call(self, account: str, tx_params=None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(account).call(tx_params)

    def send_transaction(self, account: str, tx_params=None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).transact(tx_params.as_dict())

    def build_transaction(self, account: str, tx_params=None) -> dict:
        """Construct calldata to be used as input to the method."""
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, account: str, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).estimateGas(tx_params.as_dict())


class RenounceOwnershipMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the renounceOwnership method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params=None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method().call(tx_params)

    def send_transaction(self, tx_params=None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params=None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class SeattleMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the seattle method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params=None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method().call(tx_params)

    def send_transaction(self, tx_params=None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params=None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class SetKeeperMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the setKeeper method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction, validator: Validator = None):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, addr: str):
        """Validate the inputs to the setKeeper method."""
        self.validator.assert_valid(
            method_name='setKeeper',
            parameter_name='addr',
            argument_value=addr,
        )
        addr = self.validate_and_checksum_address(addr)
        return (addr)

    def call(self, addr: str, tx_params=None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (addr) = self.validate_and_normalize_inputs(addr)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(addr).call(tx_params)

    def send_transaction(self, addr: str, tx_params=None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (addr) = self.validate_and_normalize_inputs(addr)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(addr).transact(tx_params.as_dict())

    def build_transaction(self, addr: str, tx_params=None) -> dict:
        """Construct calldata to be used as input to the method."""
        (addr) = self.validate_and_normalize_inputs(addr)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(addr).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, addr: str, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        (addr) = self.validate_and_normalize_inputs(addr)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(addr).estimateGas(tx_params.as_dict())


class SetLimitMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the setLimit method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction, validator: Validator = None):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, bonus_li: int, send_li: int, withdraw_li: int):
        """Validate the inputs to the setLimit method."""
        self.validator.assert_valid(
            method_name='setLimit',
            parameter_name='bonusLi',
            argument_value=bonus_li,
        )
        # safeguard against fractional inputs
        bonus_li = int(bonus_li)
        self.validator.assert_valid(
            method_name='setLimit',
            parameter_name='sendLi',
            argument_value=send_li,
        )
        # safeguard against fractional inputs
        send_li = int(send_li)
        self.validator.assert_valid(
            method_name='setLimit',
            parameter_name='withdrawLi',
            argument_value=withdraw_li,
        )
        # safeguard against fractional inputs
        withdraw_li = int(withdraw_li)
        return (bonus_li, send_li, withdraw_li)

    def call(self, bonus_li: int, send_li: int, withdraw_li: int, tx_params=None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (bonus_li, send_li, withdraw_li) = self.validate_and_normalize_inputs(bonus_li, send_li, withdraw_li)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(bonus_li, send_li, withdraw_li).call(tx_params)

    def send_transaction(self, bonus_li: int, send_li: int, withdraw_li: int, tx_params=None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (bonus_li, send_li, withdraw_li) = self.validate_and_normalize_inputs(bonus_li, send_li, withdraw_li)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(bonus_li, send_li, withdraw_li).transact(tx_params.as_dict())

    def build_transaction(self, bonus_li: int, send_li: int, withdraw_li: int, tx_params=None) -> dict:
        """Construct calldata to be used as input to the method."""
        (bonus_li, send_li, withdraw_li) = self.validate_and_normalize_inputs(bonus_li, send_li, withdraw_li)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(bonus_li, send_li, withdraw_li).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, bonus_li: int, send_li: int, withdraw_li: int, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        (bonus_li, send_li, withdraw_li) = self.validate_and_normalize_inputs(bonus_li, send_li, withdraw_li)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(bonus_li, send_li, withdraw_li).estimateGas(tx_params.as_dict())


class ShenzhenMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the shenzhen method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params=None) -> Tuple[int, int, int, int, int, int, int, int, int, int, int, int, int, int]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params)
        return (returned[0], returned[1], returned[2], returned[3], returned[4], returned[5], returned[6], returned[7],
                returned[8], returned[9], returned[10], returned[11], returned[12], returned[13],)

    def estimate_gas(self, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class StdCircleMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the stdCircle method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params=None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method().call(tx_params)

    def send_transaction(self, tx_params=None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params=None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class StopImportMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the stopImport method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params=None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method().call(tx_params)

    def send_transaction(self, tx_params=None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params=None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class TransferOwnershipMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the transferOwnership method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction, validator: Validator = None):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, new_owner: str):
        """Validate the inputs to the transferOwnership method."""
        self.validator.assert_valid(
            method_name='transferOwnership',
            parameter_name='newOwner',
            argument_value=new_owner,
        )
        new_owner = self.validate_and_checksum_address(new_owner)
        return (new_owner)

    def call(self, new_owner: str, tx_params=None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (new_owner) = self.validate_and_normalize_inputs(new_owner)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(new_owner).call(tx_params)

    def send_transaction(self, new_owner: str, tx_params=None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (new_owner) = self.validate_and_normalize_inputs(new_owner)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(new_owner).transact(tx_params.as_dict())

    def build_transaction(self, new_owner: str, tx_params=None) -> dict:
        """Construct calldata to be used as input to the method."""
        (new_owner) = self.validate_and_normalize_inputs(new_owner)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(new_owner).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, new_owner: str, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        (new_owner) = self.validate_and_normalize_inputs(new_owner)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(new_owner).estimateGas(tx_params.as_dict())


class VegasMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the vegas method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction, validator: Validator = None):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, invite_code: str, de_vici_code: str):
        """Validate the inputs to the vegas method."""
        self.validator.assert_valid(
            method_name='vegas',
            parameter_name='inviteCode',
            argument_value=invite_code,
        )
        self.validator.assert_valid(
            method_name='vegas',
            parameter_name='deViciCode',
            argument_value=de_vici_code,
        )
        return (invite_code, de_vici_code)

    def call(self, invite_code: str, de_vici_code: str, tx_params=None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (invite_code, de_vici_code) = self.validate_and_normalize_inputs(invite_code, de_vici_code)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(invite_code, de_vici_code).call(tx_params)

    def send_transaction(self, invite_code: str, de_vici_code: str, tx_params=None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (invite_code, de_vici_code) = self.validate_and_normalize_inputs(invite_code, de_vici_code)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(invite_code, de_vici_code).transact(tx_params.as_dict())

    def build_transaction(self, invite_code: str, de_vici_code: str, tx_params=None) -> dict:
        """Construct calldata to be used as input to the method."""
        (invite_code, de_vici_code) = self.validate_and_normalize_inputs(invite_code, de_vici_code)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(invite_code, de_vici_code).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, invite_code: str, de_vici_code: str, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        (invite_code, de_vici_code) = self.validate_and_normalize_inputs(invite_code, de_vici_code)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(invite_code, de_vici_code).estimateGas(tx_params.as_dict())


class WhatTimeMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the whatTime method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params=None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params)
        return int(returned)

    def estimate_gas(self, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class WithdrawExchangeMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the withdrawExchange method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params=None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method().call(tx_params)

    def send_transaction(self, tx_params=None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params=None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class MasonicCoal:
    """Wrapper class for MasonicCoal Solidity contract."""
    account_ex_transaction: AccountExTransactionMethod
    """Constructor-initialized instance of
    :class:`AccountExTransactionMethod`.
    """

    account_sales: AccountSalesMethod
    """Constructor-initialized instance of
    :class:`AccountSalesMethod`.
    """

    add_whitelist_admin: AddWhitelistAdminMethod
    """Constructor-initialized instance of
    :class:`AddWhitelistAdminMethod`.
    """

    bang: BangMethod
    """Constructor-initialized instance of
    :class:`BangMethod`.
    """

    can_go_to_vegas: CanGoToVegasMethod
    """Constructor-initialized instance of
    :class:`CanGoToVegasMethod`.
    """

    cap_reached: CapReachedMethod
    """Constructor-initialized instance of
    :class:`CapReachedMethod`.
    """

    compare_str: CompareStrMethod
    """Constructor-initialized instance of
    :class:`CompareStrMethod`.
    """

    confirm_invite_code: ConfirmInviteCodeMethod
    """Constructor-initialized instance of
    :class:`ConfirmInviteCodeMethod`.
    """

    contract_exists: ContractExistsMethod
    """Constructor-initialized instance of
    :class:`ContractExistsMethod`.
    """

    contract_invalidate: ContractInvalidateMethod
    """Constructor-initialized instance of
    :class:`ContractInvalidateMethod`.
    """

    credit_key: CreditKeyMethod
    """Constructor-initialized instance of
    :class:`CreditKeyMethod`.
    """

    distribute_diamonds: DistributeDiamondsMethod
    """Constructor-initialized instance of
    :class:`DistributeDiamondsMethod`.
    """

    election: ElectionMethod
    """Constructor-initialized instance of
    :class:`ElectionMethod`.
    """

    end_round: EndRoundMethod
    """Constructor-initialized instance of
    :class:`EndRoundMethod`.
    """

    end_test: EndTestMethod
    """Constructor-initialized instance of
    :class:`EndTestMethod`.
    """

    faucet: FaucetMethod
    """Constructor-initialized instance of
    :class:`FaucetMethod`.
    """

    force_cap: ForceCapMethod
    """Constructor-initialized instance of
    :class:`ForceCapMethod`.
    """

    force_ferrari: ForceFerrariMethod
    """Constructor-initialized instance of
    :class:`ForceFerrariMethod`.
    """

    fwmode: FwmodeMethod
    """Constructor-initialized instance of
    :class:`FwmodeMethod`.
    """

    generation_mulby_lv: GenerationMulbyLvMethod
    """Constructor-initialized instance of
    :class:`GenerationMulbyLvMethod`.
    """

    get_emc: GetEmcMethod
    """Constructor-initialized instance of
    :class:`GetEmcMethod`.
    """

    get_level: GetLevelMethod
    """Constructor-initialized instance of
    :class:`GetLevelMethod`.
    """

    get_line_user_id: GetLineUserIdMethod
    """Constructor-initialized instance of
    :class:`GetLineUserIdMethod`.
    """

    get_node_level: GetNodeLevelMethod
    """Constructor-initialized instance of
    :class:`GetNodeLevelMethod`.
    """

    get_user_address_by_code: GetUserAddressByCodeMethod
    """Constructor-initialized instance of
    :class:`GetUserAddressByCodeMethod`.
    """

    get_user_address_by_id: GetUserAddressByIdMethod
    """Constructor-initialized instance of
    :class:`GetUserAddressByIdMethod`.
    """

    get_user_by_address: GetUserByAddressMethod
    """Constructor-initialized instance of
    :class:`GetUserByAddressMethod`.
    """

    ginza: GinzaMethod
    """Constructor-initialized instance of
    :class:`GinzaMethod`.
    """

    import_member: ImportMemberMethod
    """Constructor-initialized instance of
    :class:`ImportMemberMethod`.
    """

    input_reward_by_lv: InputRewardByLvMethod
    """Constructor-initialized instance of
    :class:`InputRewardByLvMethod`.
    """

    is_blueprint: IsBlueprintMethod
    """Constructor-initialized instance of
    :class:`IsBlueprintMethod`.
    """

    is_owner: IsOwnerMethod
    """Constructor-initialized instance of
    :class:`IsOwnerMethod`.
    """

    is_whitelist_admin: IsWhitelistAdminMethod
    """Constructor-initialized instance of
    :class:`IsWhitelistAdminMethod`.
    """

    linedeposit: LinedepositMethod
    """Constructor-initialized instance of
    :class:`LinedepositMethod`.
    """

    nagoya: NagoyaMethod
    """Constructor-initialized instance of
    :class:`NagoyaMethod`.
    """

    node_rewardby_lv: NodeRewardbyLvMethod
    """Constructor-initialized instance of
    :class:`NodeRewardbyLvMethod`.
    """

    owner: OwnerMethod
    """Constructor-initialized instance of
    :class:`OwnerMethod`.
    """

    release_diamonds: ReleaseDiamondsMethod
    """Constructor-initialized instance of
    :class:`ReleaseDiamondsMethod`.
    """

    remove_whitelist_admin: RemoveWhitelistAdminMethod
    """Constructor-initialized instance of
    :class:`RemoveWhitelistAdminMethod`.
    """

    renounce_ownership: RenounceOwnershipMethod
    """Constructor-initialized instance of
    :class:`RenounceOwnershipMethod`.
    """

    seattle: SeattleMethod
    """Constructor-initialized instance of
    :class:`SeattleMethod`.
    """

    set_keeper: SetKeeperMethod
    """Constructor-initialized instance of
    :class:`SetKeeperMethod`.
    """

    set_limit: SetLimitMethod
    """Constructor-initialized instance of
    :class:`SetLimitMethod`.
    """

    shenzhen: ShenzhenMethod
    """Constructor-initialized instance of
    :class:`ShenzhenMethod`.
    """

    std_circle: StdCircleMethod
    """Constructor-initialized instance of
    :class:`StdCircleMethod`.
    """

    stop_import: StopImportMethod
    """Constructor-initialized instance of
    :class:`StopImportMethod`.
    """

    transfer_ownership: TransferOwnershipMethod
    """Constructor-initialized instance of
    :class:`TransferOwnershipMethod`.
    """

    vegas: VegasMethod
    """Constructor-initialized instance of
    :class:`VegasMethod`.
    """

    what_time: WhatTimeMethod
    """Constructor-initialized instance of
    :class:`WhatTimeMethod`.
    """

    withdraw_exchange: WithdrawExchangeMethod
    """Constructor-initialized instance of
    :class:`WithdrawExchangeMethod`.
    """

    def __init__(
            self,
            tron_provider: Tron,
            contract_address: str,
            validator: MasonicCoalValidator = None,
    ):
        """Get an instance of wrapper for smart contract.

        :param tron_provider: Either an instance of `web3.Web3`:code: or
            `web3.providers.base.BaseProvider`:code:
        :param contract_address: where the contract has been deployed
        :param validator: for validation of method inputs.
        """
        # pylint: disable=too-many-statements

        self.contract_address = contract_address

        if not validator:
            validator = MasonicCoalValidator(tron_provider, contract_address)

        # if any middleware was imported, inject it
        try:
            MIDDLEWARE
        except NameError:
            pass
        else:
            try:
                for middleware in MIDDLEWARE:
                    web3.middleware_onion.inject(
                        middleware['function'], layer=middleware['layer'],
                    )
            except ValueError as value_error:
                if value_error.args == ("You can't add the same un-named instance twice",):
                    pass

        self._tron_trx = tron_provider.trx

        abi_dict = MasonicCoal.abi()
        contract = self._tron_trx.contract(address=contract_address, abi=abi_dict)
        owner = self._tron_trx.tron.default_address
        fn = contract.functions

        self.account_ex_transaction = AccountExTransactionMethod(
            fn.get_abi_by_name('accountExTransaction'),
            contract,
            owner,
            contract_address,
            fn.accountExTransaction, validator)
        self.account_sales = AccountSalesMethod(
            fn.get_abi_by_name('accountSales'),
            contract,
            owner,
            contract_address,
            fn.accountSales, validator)
        self.add_whitelist_admin = AddWhitelistAdminMethod(
            fn.get_abi_by_name('addWhitelistAdmin'),
            contract,
            owner,
            contract_address,
            fn.addWhitelistAdmin, validator)
        self.bang = BangMethod(
            fn.get_abi_by_name('bang'),
            contract,
            owner,
            contract_address,
            fn.bang, validator)
        self.can_go_to_vegas = CanGoToVegasMethod(
            fn.get_abi_by_name('canGoToVegas'),
            contract,
            owner,
            contract_address,
            fn.canGoToVegas)
        self.cap_reached = CapReachedMethod(
            fn.get_abi_by_name('capReached'),
            contract,
            owner,
            contract_address,
            fn.capReached, validator)
        self.compare_str = CompareStrMethod(
            fn.get_abi_by_name('compareStr'),
            contract,
            owner,
            contract_address,
            fn.compareStr, validator)
        self.confirm_invite_code = ConfirmInviteCodeMethod(
            fn.get_abi_by_name('confirmInviteCode'),
            contract,
            owner,
            contract_address,
            fn.confirmInviteCode, validator)
        self.contract_exists = ContractExistsMethod(
            fn.get_abi_by_name('contractExists'),
            contract,
            owner,
            contract_address,
            fn.contractExists, validator)
        self.contract_invalidate = ContractInvalidateMethod(
            fn.get_abi_by_name('contractInvalidate'),
            contract,
            owner,
            contract_address,
            fn.contractInvalidate)
        self.credit_key = CreditKeyMethod(
            fn.get_abi_by_name('creditKey'),
            contract,
            owner,
            contract_address,
            fn.creditKey, validator)
        self.distribute_diamonds = DistributeDiamondsMethod(
            fn.get_abi_by_name('distribute_diamonds'),
            contract,
            owner,
            contract_address,
            fn.distribute_diamonds, validator)
        self.election = ElectionMethod(
            fn.get_abi_by_name('election'),
            contract,
            owner,
            contract_address,
            fn.election)
        self.end_round = EndRoundMethod(
            fn.get_abi_by_name('endRound'),
            contract,
            owner,
            contract_address,
            fn.endRound)
        self.end_test = EndTestMethod(
            fn.get_abi_by_name('endTest'),
            contract,
            owner,
            contract_address,
            fn.endTest)
        self.faucet = FaucetMethod(
            fn.get_abi_by_name('faucet'),
            contract,
            owner,
            contract_address,
            fn.faucet, validator)
        self.force_cap = ForceCapMethod(
            fn.get_abi_by_name('forceCap'),
            contract,
            owner,
            contract_address,
            fn.forceCap, validator)
        self.force_ferrari = ForceFerrariMethod(
            fn.get_abi_by_name('forceFerrari'),
            contract,
            owner,
            contract_address,
            fn.forceFerrari, validator)
        self.fwmode = FwmodeMethod(
            fn.get_abi_by_name('fwmode'),
            contract,
            owner,
            contract_address,
            fn.fwmode)
        self.generation_mulby_lv = GenerationMulbyLvMethod(
            fn.get_abi_by_name('generationMulbyLv'),
            contract,
            owner,
            contract_address,
            fn.generationMulbyLv, validator)
        self.get_emc = GetEmcMethod(
            fn.get_abi_by_name('getEmc'),
            contract,
            owner,
            contract_address,
            fn.getEmc, validator)
        self.get_level = GetLevelMethod(
            fn.get_abi_by_name('getLevel'),
            contract,
            owner,
            contract_address,
            fn.getLevel, validator)
        self.get_line_user_id = GetLineUserIdMethod(
            fn.get_abi_by_name('getLineUserId'),
            contract,
            owner,
            contract_address,
            fn.getLineUserId, validator)
        self.get_node_level = GetNodeLevelMethod(
            fn.get_abi_by_name('getNodeLevel'),
            contract,
            owner,
            contract_address,
            fn.getNodeLevel, validator)
        self.get_user_address_by_code = GetUserAddressByCodeMethod(
            fn.get_abi_by_name('getUserAddressByCode'),
            contract,
            owner,
            contract_address,
            fn.getUserAddressByCode, validator)
        self.get_user_address_by_id = GetUserAddressByIdMethod(
            fn.get_abi_by_name('getUserAddressById'),
            contract,
            owner,
            contract_address,
            fn.getUserAddressById, validator)
        self.get_user_by_address = GetUserByAddressMethod(
            fn.get_abi_by_name('getUserByAddress'),
            contract,
            owner,
            contract_address,
            fn.getUserByAddress, validator)
        self.ginza = GinzaMethod(
            fn.get_abi_by_name('ginza'),
            contract,
            owner,
            contract_address,
            fn.ginza, validator)
        self.import_member = ImportMemberMethod(
            fn.get_abi_by_name('importMember'),
            contract,
            owner,
            contract_address,
            fn.importMember, validator)
        self.input_reward_by_lv = InputRewardByLvMethod(
            fn.get_abi_by_name('inputRewardByLv'),
            contract,
            owner,
            contract_address,
            fn.inputRewardByLv, validator)
        self.is_blueprint = IsBlueprintMethod(
            fn.get_abi_by_name('isBlueprint'),
            contract,
            owner,
            contract_address,
            fn.isBlueprint)
        self.is_owner = IsOwnerMethod(
            fn.get_abi_by_name('isOwner'),
            contract,
            owner,
            contract_address,
            fn.isOwner)
        self.is_whitelist_admin = IsWhitelistAdminMethod(
            fn.get_abi_by_name('isWhitelistAdmin'),
            contract,
            owner,
            contract_address,
            fn.isWhitelistAdmin, validator)
        self.linedeposit = LinedepositMethod(
            fn.get_abi_by_name('linedeposit'),
            contract,
            owner,
            contract_address,
            fn.linedeposit, validator)
        self.nagoya = NagoyaMethod(
            fn.get_abi_by_name('nagoya'),
            contract,
            owner,
            contract_address,
            fn.nagoya, validator)
        self.node_rewardby_lv = NodeRewardbyLvMethod(
            fn.get_abi_by_name('nodeRewardbyLv'),
            contract,
            owner,
            contract_address,
            fn.nodeRewardbyLv, validator)
        self.owner = OwnerMethod(
            fn.get_abi_by_name('owner'),
            contract,
            owner,
            contract_address,
            fn.owner)
        self.release_diamonds = ReleaseDiamondsMethod(
            fn.get_abi_by_name('releaseDiamonds'),
            contract,
            owner,
            contract_address,
            fn.releaseDiamonds, validator)
        self.remove_whitelist_admin = RemoveWhitelistAdminMethod(
            fn.get_abi_by_name('removeWhitelistAdmin'),
            contract,
            owner,
            contract_address,
            fn.removeWhitelistAdmin, validator)
        self.renounce_ownership = RenounceOwnershipMethod(
            fn.get_abi_by_name('renounceOwnership'),
            contract,
            owner,
            contract_address,
            fn.renounceOwnership)
        self.seattle = SeattleMethod(
            fn.get_abi_by_name('seattle'),
            contract,
            owner,
            contract_address,
            fn.seattle)
        self.set_keeper = SetKeeperMethod(
            fn.get_abi_by_name('setKeeper'),
            contract,
            owner,
            contract_address,
            fn.setKeeper, validator)
        self.set_limit = SetLimitMethod(
            fn.get_abi_by_name('setLimit'),
            contract,
            owner,
            contract_address,
            fn.setLimit, validator)
        self.shenzhen = ShenzhenMethod(
            fn.get_abi_by_name('shenzhen'),
            contract,
            owner,
            contract_address,
            fn.shenzhen)
        self.std_circle = StdCircleMethod(
            fn.get_abi_by_name('stdCircle'),
            contract,
            owner,
            contract_address,
            fn.stdCircle)
        self.stop_import = StopImportMethod(
            fn.get_abi_by_name('stopImport'),
            contract,
            owner,
            contract_address,
            fn.stopImport)
        self.transfer_ownership = TransferOwnershipMethod(
            fn.get_abi_by_name('transferOwnership'),
            contract,
            owner,
            contract_address,
            fn.transferOwnership, validator)
        self.vegas = VegasMethod(
            fn.get_abi_by_name('vegas'),
            contract,
            owner,
            contract_address,
            fn.vegas, validator)
        self.what_time = WhatTimeMethod(
            fn.get_abi_by_name('whatTime'),
            contract,
            owner,
            contract_address,
            fn.whatTime)
        self.withdraw_exchange = WithdrawExchangeMethod(
            fn.get_abi_by_name('withdrawExchange'),
            contract,
            owner,
            contract_address,
            fn.withdrawExchange)

    def get_change_config_event(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ChangeConfig event.

        :param tx_hash: hash of transaction emitting ChangeConfig event
        """
        tx_receipt = self.trackEventReceipt(tx_hash)
        return tx_receipt

    def get_clock_tower_event(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ClockTower event.

        :param tx_hash: hash of transaction emitting ClockTower event
        """
        tx_receipt = self.trackEventReceipt(tx_hash)
        return tx_receipt

    def get_end_round_event(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for EndRound event.

        :param tx_hash: hash of transaction emitting EndRound event
        """
        tx_receipt = self.trackEventReceipt(tx_hash)
        return tx_receipt

    def get_exchange_success_event(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ExchangeSuccess event.

        :param tx_hash: hash of transaction emitting ExchangeSuccess event
        """
        tx_receipt = self.trackEventReceipt(tx_hash)
        return tx_receipt

    def get_limit_changed_event(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for LimitChanged event.

        :param tx_hash: hash of transaction emitting LimitChanged event
        """
        tx_receipt = self.trackEventReceipt(tx_hash)
        return tx_receipt

    def get_not_enough_to_send_event(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for NotEnoughToSend event.

        :param tx_hash: hash of transaction emitting NotEnoughToSend event
        """
        tx_receipt = self.trackEventReceipt(tx_hash)
        return tx_receipt

    def get_ownership_transferred_event(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for OwnershipTransferred event.

        :param tx_hash: hash of transaction emitting OwnershipTransferred event
        """
        tx_receipt = self.trackEventReceipt(tx_hash)
        return tx_receipt

    def get_pre_end_event(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for PreEnd event.

        :param tx_hash: hash of transaction emitting PreEnd event
        """
        tx_receipt = self.trackEventReceipt(tx_hash)
        return tx_receipt

    def get_release_signal_event(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ReleaseSignal event.

        :param tx_hash: hash of transaction emitting ReleaseSignal event
        """
        tx_receipt = self.trackEventReceipt(tx_hash)
        return tx_receipt

    @staticmethod
    def abi() -> dict:
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"string","name":"t","type":"string"}],"name":"ChangeConfig","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"d1","type":"address"},{"indexed":false,"internalType":"address","name":"d2","type":"address"},{"indexed":false,"internalType":"uint256","name":"a","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"b","type":"uint256"}],"name":"ClockTower","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"a","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"b","type":"uint256"}],"name":"EndRound","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"boss","type":"address"},{"indexed":false,"internalType":"address","name":"target","type":"address"},{"indexed":false,"internalType":"address","name":"buyer","type":"address"},{"indexed":false,"internalType":"uint256","name":"commission","type":"uint256"}],"name":"ExchangeSuccess","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"a","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"b","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"c","type":"uint256"}],"name":"LimitChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"d1","type":"address"},{"indexed":false,"internalType":"uint256","name":"d2","type":"uint256"}],"name":"NotEnoughToSend","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"lastlucky","type":"address"}],"name":"PreEnd","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"ReleaseSignal","type":"event"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"constant":false,"inputs":[{"internalType":"address","name":"seller_account","type":"address"},{"internalType":"address","name":"buyer_account","type":"address"}],"name":"accountExTransaction","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"sales_amount","type":"uint256"}],"name":"accountSales","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"addWhitelistAdmin","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"time","type":"uint256"}],"name":"bang","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"canGoToVegas","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"che","type":"address"}],"name":"capReached","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"string","name":"src","type":"string"},{"internalType":"string","name":"src_compared","type":"string"}],"name":"compareStr","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"string","name":"code","type":"string"}],"name":"confirmInviteCode","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"contractc","type":"address"}],"name":"contractExists","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"contractInvalidate","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"member","type":"address"}],"name":"creditKey","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"balance","type":"uint256"}],"name":"distribute_diamonds","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"election","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"endRound","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"endTest","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"start","type":"uint256"},{"internalType":"uint256","name":"end","type":"uint256"}],"name":"faucet","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"v","type":"uint256"}],"name":"forceCap","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"k","type":"uint256"}],"name":"forceFerrari","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"fwmode","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"level","type":"uint256"},{"internalType":"uint256","name":"times","type":"uint256"}],"name":"generationMulbyLv","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"value","type":"uint256"}],"name":"getEmc","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"value","type":"uint256"}],"name":"getLevel","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"index","type":"uint256"},{"internalType":"uint256","name":"rouId","type":"uint256"}],"name":"getLineUserId","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"value","type":"uint256"}],"name":"getNodeLevel","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"string","name":"code","type":"string"}],"name":"getUserAddressByCode","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"getUserAddressById","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"member","type":"address"},{"internalType":"uint256","name":"roundId","type":"uint256"}],"name":"getUserByAddress","outputs":[{"internalType":"uint256[17]","name":"info","type":"uint256[17]"},{"internalType":"string","name":"inviteCode","type":"string"},{"internalType":"string","name":"deViciCode","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"addr","type":"address"},{"internalType":"uint256","name":"status","type":"uint256"}],"name":"ginza","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"addr","type":"address"},{"internalType":"string","name":"inviteCode","type":"string"},{"internalType":"string","name":"deViciCode","type":"string"}],"name":"importMember","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"level","type":"uint256"}],"name":"inputRewardByLv","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[],"name":"isBlueprint","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"isOwner","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"isWhitelistAdmin","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"start","type":"uint256"},{"internalType":"uint256","name":"end","type":"uint256"}],"name":"linedeposit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"line","type":"uint256"}],"name":"nagoya","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"level","type":"uint256"}],"name":"nodeRewardbyLv","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"m1","type":"address"},{"internalType":"address","name":"m2","type":"address"},{"internalType":"address[]","name":"luck_members","type":"address[]"}],"name":"releaseDiamonds","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"removeWhitelistAdmin","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"renounceOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"seattle","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"addr","type":"address"}],"name":"setKeeper","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"bonusLi","type":"uint256"},{"internalType":"uint256","name":"sendLi","type":"uint256"},{"internalType":"uint256","name":"withdrawLi","type":"uint256"}],"name":"setLimit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"shenzhen","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"stdCircle","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"stopImport","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"string","name":"inviteCode","type":"string"},{"internalType":"string","name":"deViciCode","type":"string"}],"name":"vegas","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[],"name":"whatTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"withdrawExchange","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]'
            # noqa: E501 (line-too-long)
        )

# pylint: disable=too-many-lines
