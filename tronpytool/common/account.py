# --------------------------------------------------------------------
# Copyright (c) fInvention.c. All rights reserved.
# Licensed under the MIT License.
# See License.txt in the project root for license information.
# --------------------------------------------------------------------

import codecs
from binascii import unhexlify

import base58
import ecdsa
from eth_account import Account as ETHAccount
from eth_keys import KeyAPI
from eth_utils import keccak
from trx_utils import is_hex, is_bytes

from tronpytool.common.datastructures import AttributeDict
from tronpytool.common.key import PrivateKey as PFactory


class Account:

    def generate_address(self, priv_key=None) -> dict:
        """Generate a random address."""
        if priv_key is None:
            priv_key = PFactory.random()
        return {
            "base58check_address": priv_key.public_key.to_base58check_address(),
            "hex_address": priv_key.public_key.to_hex_address(),
            "private_key": priv_key.hex(),
            "public_key": priv_key.public_key.hex(),
        }

    def get_address_from_passphrase(self, passphrase: str) -> dict:
        """Get an address from a passphrase, compatiable with `wallet/createaddress`."""
        priv_key = PFactory.from_passphrase(passphrase.encode())
        return self.generate_address(priv_key)

    @staticmethod
    def create():
        generate_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
        return PrivateKey(generate_key.to_string().hex())

    @staticmethod
    def sign_hash(message_hash, private_key):
        if not is_hex(message_hash):
            raise ValueError('Invalid message_hash provided')

        return ETHAccount.signHash(message_hash, private_key)

    @staticmethod
    def recover_hash(message_hash, signature):
        if not is_hex(message_hash):
            raise ValueError('Invalid message_hash provided')

        return ETHAccount.recoverHash(message_hash, signature=signature)


class Address:

    @staticmethod
    def from_hex(address) -> str:
        """Helper function that will convert a generic value from hex"""
        if not is_hex(address):
            return address
        return base58.b58encode_check(bytes.fromhex(address)).decode()

    @staticmethod
    def to_hex(address) -> str:
        """Helper function that will convert a generic value to hex"""
        if is_hex(address):
            return address.lower().replace('0x', '41', 2)
        return base58.b58decode_check(address).hex().upper()

    @staticmethod
    def to_hex_0x(address) -> str:
        """Helper function that will convert a generic value to hex"""
        if is_hex(address):
            return address
        return '0x' + base58.b58decode_check(address).hex().upper()[2:]

    @staticmethod
    def to_hex_check_sum(address) -> str:
        """Helper function that will convert a generic value to hex"""
        if is_hex(address):
            return address
        step1 = base58.b58decode_check(address).hex().lower()[2:]
        print(address)
        print(step1)
        return Address.checksum_encode(step1)

    @staticmethod
    def checksum_encode(hex_addr: str) -> str:  # Takes a 20-byte binary address as input
        # hex_addr = addr.hex()
        checksummed_buffer = ""
        # Treat the hex address as ascii/utf-8 for keccak256 hashing
        hashed_address = keccak(text=hex_addr).hex()

        # Iterate over each character in the hex address
        for nibble_index, character in enumerate(hex_addr):
            if character in "0123456789":
                # We can't upper-case the decimal digits
                checksummed_buffer += character
            elif character in "abcdef":
                # Check if the corresponding hex digit (nibble) in the hash is 8 or higher
                hashed_address_nibble = int(hashed_address[nibble_index], 16)
                if hashed_address_nibble > 7:
                    checksummed_buffer += character.upper()
                else:
                    checksummed_buffer += character
            else:
                raise TypeError(f"Unrecognized hex character {character!r} at position {nibble_index}")
        print("----- now up", checksummed_buffer)
        return "0x" + checksummed_buffer

    @staticmethod
    def to_hex_0x_41(address) -> str:
        """Helper function that will convert a generic value to hex"""
        if is_hex(address):
            return address
        return '0x' + base58.b58decode_check(address).hex().upper()

    @staticmethod
    def from_private_key(private_key) -> AttributeDict:
        return PrivateKey(private_key).address


class PrivateKey(object):

    def __init__(self, private_key: str):
        """Work with private key.
        Getting: PublicKey, PublicToAddress

        Example:::
            PrivateKey("4d1bc37b069b9f2e975c37770b7c87185dc3a10454e3ea024ce1fce8f3eb78bf")
        """
        if private_key is None:
            raise ValueError('Empty private key here')

        _private = unhexlify(bytes(private_key, encoding='utf8'))
        self._key = KeyAPI.PrivateKey(_private)
        self.stored_privkey = private_key
        _length = len(self._key)

        # Key length must not exceed 64 length
        if _length < 64:
            raise ValueError('Key length must not exceed 64 length')

    @property
    def private_key(self) -> str:
        _raw_key = self._key.to_bytes()
        return codecs.decode(codecs.encode(_raw_key, 'hex'), 'ascii')

    @property
    def public_key(self) -> str:
        public_key = self._key.public_key
        return '04' + str(public_key)[2:]

    @property
    def address(self) -> AttributeDict:
        public_key = self._key.public_key
        address = '41' + public_key.to_address()[2:]
        contract_address = '0x' + public_key.to_address()[2:]
        to_base58 = base58.b58encode_check(bytes.fromhex(address))
        # If bytecode then convert to string
        if is_bytes(to_base58):
            to_base58 = to_base58.decode()

        return AttributeDict({
            'hex': address,
            'base58': to_base58,
            'sol': contract_address
        })

    def printKeys(self):
        pair = self.address
        print("public hex: {}".format(pair.hex))
        print("public wallet address in base58: {}".format(pair.base58))
        print("public address in contract: {}".format(pair.sol))

    def __str__(self):
        return self.stored_privkey

    def __bytes__(self):
        return self._key.to_bytes()
