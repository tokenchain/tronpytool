#!/usr/bin/env python
# coding: utf-8

"""Generated wrapper for BonusKeep Solidity contract."""

# pylint: disable=too-many-arguments

import json
from typing import (  # pylint: disable=unused-import
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
# constructor for BonusKeep below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        BonusKeepValidator,
    )
except ImportError:

    class BonusKeepValidator(  # type: ignore
        Validator
    ):
        """No-op input validator."""

try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class BasicBalanceReqsMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the basic_balance_reqs method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction, validator: Validator = None):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, a: int, b: int):
        """Validate the inputs to the basic_balance_reqs method."""
        self.validator.assert_valid(
            method_name='basic_balance_reqs',
            parameter_name='a',
            argument_value=a,
        )
        # safeguard against fractional inputs
        a = int(a)
        self.validator.assert_valid(
            method_name='basic_balance_reqs',
            parameter_name='b',
            argument_value=b,
        )
        # safeguard against fractional inputs
        b = int(b)
        return (a, b)

    def call(self, a: int, b: int, tx_params=None) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (a, b) = self.validate_and_normalize_inputs(a, b)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(a, b).call(tx_params)
        return bool(returned)

    def estimate_gas(self, a: int, b: int, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        (a, b) = self.validate_and_normalize_inputs(a, b)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(a, b).estimateGas(tx_params.as_dict())


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


class EnsureMoneySendableMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the ensure_money_sendable method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction, validator: Validator = None):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, send_money: int, balance: int, prize_balance: int):
        """Validate the inputs to the ensure_money_sendable method."""
        self.validator.assert_valid(
            method_name='ensure_money_sendable',
            parameter_name='send_money',
            argument_value=send_money,
        )
        # safeguard against fractional inputs
        send_money = int(send_money)
        self.validator.assert_valid(
            method_name='ensure_money_sendable',
            parameter_name='balance',
            argument_value=balance,
        )
        # safeguard against fractional inputs
        balance = int(balance)
        self.validator.assert_valid(
            method_name='ensure_money_sendable',
            parameter_name='prizeBalance',
            argument_value=prize_balance,
        )
        # safeguard against fractional inputs
        prize_balance = int(prize_balance)
        return (send_money, balance, prize_balance)

    def call(self, send_money: int, balance: int, prize_balance: int, tx_params=None) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (send_money, balance, prize_balance) = self.validate_and_normalize_inputs(send_money, balance, prize_balance)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(send_money, balance, prize_balance).call(tx_params)
        return bool(returned)

    def estimate_gas(self, send_money: int, balance: int, prize_balance: int, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        (send_money, balance, prize_balance) = self.validate_and_normalize_inputs(send_money, balance, prize_balance)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(send_money, balance, prize_balance).estimateGas(tx_params.as_dict())


class ExchangeHandlingSplitMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the exchange_handling_split method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction, validator: Validator = None):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, amount: int):
        """Validate the inputs to the exchange_handling_split method."""
        self.validator.assert_valid(
            method_name='exchange_handling_split',
            parameter_name='amount',
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        return (amount)

    def call(self, amount: int, tx_params=None) -> Tuple[int, int]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (amount) = self.validate_and_normalize_inputs(amount)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(amount).call(tx_params)
        return (returned[0], returned[1],)

    def estimate_gas(self, amount: int, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        (amount) = self.validate_and_normalize_inputs(amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(amount).estimateGas(tx_params.as_dict())


class FaucetPoolSplitMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the faucet_pool_split method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction, validator: Validator = None):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, amount: int):
        """Validate the inputs to the faucet_pool_split method."""
        self.validator.assert_valid(
            method_name='faucet_pool_split',
            parameter_name='amount',
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        return (amount)

    def call(self, amount: int, tx_params=None) -> Tuple[int, int]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (amount) = self.validate_and_normalize_inputs(amount)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(amount).call(tx_params)
        return (returned[0], returned[1],)

    def estimate_gas(self, amount: int, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        (amount) = self.validate_and_normalize_inputs(amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(amount).estimateGas(tx_params.as_dict())


class PositiveBalanceMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the positiveBalance method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction, validator: Validator = None):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, balance: int, prize_balance: int):
        """Validate the inputs to the positiveBalance method."""
        self.validator.assert_valid(
            method_name='positiveBalance',
            parameter_name='balance',
            argument_value=balance,
        )
        # safeguard against fractional inputs
        balance = int(balance)
        self.validator.assert_valid(
            method_name='positiveBalance',
            parameter_name='prizeBalance',
            argument_value=prize_balance,
        )
        # safeguard against fractional inputs
        prize_balance = int(prize_balance)
        return (balance, prize_balance)

    def call(self, balance: int, prize_balance: int, tx_params=None) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (balance, prize_balance) = self.validate_and_normalize_inputs(balance, prize_balance)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(balance, prize_balance).call(tx_params)
        return bool(returned)

    def estimate_gas(self, balance: int, prize_balance: int, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        (balance, prize_balance) = self.validate_and_normalize_inputs(balance, prize_balance)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(balance, prize_balance).estimateGas(tx_params.as_dict())


class ResidualCoverMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the residual_cover method."""

    def __init__(self, abi: dict, contract: Contract, owner_address: str, contract_address: str,
                 contract_function: ContractFunction, validator: Validator = None):
        """Persist instance data."""
        super().__init__(abi, contract, owner_address, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, balance: int, prize_balance: int):
        """Validate the inputs to the residual_cover method."""
        self.validator.assert_valid(
            method_name='residual_cover',
            parameter_name='balance',
            argument_value=balance,
        )
        # safeguard against fractional inputs
        balance = int(balance)
        self.validator.assert_valid(
            method_name='residual_cover',
            parameter_name='prizeBalance',
            argument_value=prize_balance,
        )
        # safeguard against fractional inputs
        prize_balance = int(prize_balance)
        return (balance, prize_balance)

    def call(self, balance: int, prize_balance: int, tx_params=None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters

        """
        (balance, prize_balance) = self.validate_and_normalize_inputs(balance, prize_balance)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(balance, prize_balance).call(tx_params)
        return int(returned)

    def estimate_gas(self, balance: int, prize_balance: int, tx_params=None) -> int:
        """Estimate gas consumption of method call."""
        (balance, prize_balance) = self.validate_and_normalize_inputs(balance, prize_balance)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(balance, prize_balance).estimateGas(tx_params.as_dict())


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class BonusKeep:
    """Wrapper class for BonusKeep Solidity contract."""
    basic_balance_reqs: BasicBalanceReqsMethod
    """Constructor-initialized instance of
    :class:`BasicBalanceReqsMethod`.
    """

    distribute_diamonds: DistributeDiamondsMethod
    """Constructor-initialized instance of
    :class:`DistributeDiamondsMethod`.
    """

    ensure_money_sendable: EnsureMoneySendableMethod
    """Constructor-initialized instance of
    :class:`EnsureMoneySendableMethod`.
    """

    exchange_handling_split: ExchangeHandlingSplitMethod
    """Constructor-initialized instance of
    :class:`ExchangeHandlingSplitMethod`.
    """

    faucet_pool_split: FaucetPoolSplitMethod
    """Constructor-initialized instance of
    :class:`FaucetPoolSplitMethod`.
    """

    positive_balance: PositiveBalanceMethod
    """Constructor-initialized instance of
    :class:`PositiveBalanceMethod`.
    """

    residual_cover: ResidualCoverMethod
    """Constructor-initialized instance of
    :class:`ResidualCoverMethod`.
    """

    def __init__(
            self,
            tron_provider: Tron,
            contract_address: str,
            validator: BonusKeepValidator = None,
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
            validator = BonusKeepValidator(tron_provider, contract_address)

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

        abi_dict = BonusKeep.abi()
        contract = self._tron_trx.contract(address=contract_address, abi=abi_dict)
        owner = self._tron_trx.tron.default_address
        fn = contract.functions

        self.basic_balance_reqs = BasicBalanceReqsMethod(
            fn.get_abi_by_name('basic_balance_reqs'),
            contract,
            owner,
            contract_address,
            fn.basic_balance_reqs, validator)
        self.distribute_diamonds = DistributeDiamondsMethod(
            fn.get_abi_by_name('distribute_diamonds'),
            contract,
            owner,
            contract_address,
            fn.distribute_diamonds, validator)
        self.ensure_money_sendable = EnsureMoneySendableMethod(
            fn.get_abi_by_name('ensure_money_sendable'),
            contract,
            owner,
            contract_address,
            fn.ensure_money_sendable, validator)
        self.exchange_handling_split = ExchangeHandlingSplitMethod(
            fn.get_abi_by_name('exchange_handling_split'),
            contract,
            owner,
            contract_address,
            fn.exchange_handling_split, validator)
        self.faucet_pool_split = FaucetPoolSplitMethod(
            fn.get_abi_by_name('faucet_pool_split'),
            contract,
            owner,
            contract_address,
            fn.faucet_pool_split, validator)
        self.positive_balance = PositiveBalanceMethod(
            fn.get_abi_by_name('positiveBalance'),
            contract,
            owner,
            contract_address,
            fn.positiveBalance, validator)
        self.residual_cover = ResidualCoverMethod(
            fn.get_abi_by_name('residual_cover'),
            contract,
            owner,
            contract_address,
            fn.residual_cover, validator)

    def get_change_config_event(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ChangeConfig event.

        :param tx_hash: hash of transaction emitting ChangeConfig event
        """
        tx_receipt = self.trackEventReceipt(tx_hash)
        return tx_receipt

    @staticmethod
    def abi() -> dict:
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"anonymous":false,"inputs":[{"indexed":false,"internalType":"string","name":"t","type":"string"}],"name":"ChangeConfig","type":"event"},{"constant":true,"inputs":[{"internalType":"uint256","name":"a","type":"uint256"},{"internalType":"uint256","name":"b","type":"uint256"}],"name":"basic_balance_reqs","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"balance","type":"uint256"}],"name":"distribute_diamonds","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"send_money","type":"uint256"},{"internalType":"uint256","name":"balance","type":"uint256"},{"internalType":"uint256","name":"prizeBalance","type":"uint256"}],"name":"ensure_money_sendable","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"exchange_handling_split","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"faucet_pool_split","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"balance","type":"uint256"},{"internalType":"uint256","name":"prizeBalance","type":"uint256"}],"name":"positiveBalance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"balance","type":"uint256"},{"internalType":"uint256","name":"prizeBalance","type":"uint256"}],"name":"residual_cover","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"}]'
            # noqa: E501 (line-too-long)
        )

# pylint: disable=too-many-lines
