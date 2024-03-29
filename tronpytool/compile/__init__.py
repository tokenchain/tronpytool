#!/usr/bin/env python

REC = """#!/bin/bash

if [[ ! -f {TARGET_LOC} ]]; then
    mkdir -p {TARGET_LOC}/vault
fi
if [[ ! -f {TARGET_LOC}/build ]]; then
    mkdir -p {TARGET_LOC}/build
fi
#chown -R www {TARGET_LOC}/vault
cd {TARGET_LOC}
echo "🍜 changed permission to root"
SOLC_VERSION={SOLVER} solc --version

echo "and then the compiler version should be... "

{LISTP}

cd {TARGET_LOC}/build && tar -czf {COMPRESSED_NAME} *.*
mv {COMPRESSED_NAME} {TARGET_LOC}
rm -rf {TARGET_LOC}/vault
rm -rf {TARGET_LOC}/build

exit

"""

TRANS_LOCAL = """#!/bin/bash

# -----------------------------------------------
{PRE_HEAD}

{LISTP}

{FOOTER}
"""
ITEM = """
echo "🍯 Compiling from {COMPILE_COIN} 🧀"
SOLC_VERSION={SOLVER} solc --evm-version {EVMVERSION} --allow-paths {SOLCPATH} -o build --bin --bin-runtime --abi --optimize --metadata --overwrite {COMPILE_COIN}
echo "=> 🍺🍺🍺 {COMPILE_COIN}"
"""

ITEMLINK = """
echo "🍰 Compiling with LINK from {COMPILE_COIN} 🧀"
#solc --optimize --bin MetaCoin.sol | solc --link --libraries TestLib:<address>
SOLC_VERSION={SOLVER} solc --allow-paths {SOLCPATH} -o build  --optimize --bin --abi --link --libraries "{FILES_CONFIG}" --overwrite {COMPILE_COIN}
echo "=> 🍥🍥🍥 {COMPILE_COIN}"
"""

ITEM_CP_LOCAL = """
rm "{tolocation}"
cp "{fromlocation}" "{tolocation}"
"""

ITEM_TRANSPILE_PYTHON = """
if [[ ! -f {outputfolder} ]]; then
    mkdir -p {outputfolder}
fi
echo "==> 🚸 compile abi to python: {target_abi} / {outputfolder}"
abi-gen-uni --abibins {target_abi} --out "{outputfolder}" \
    --partials "{BUILDPATH}/factoryabi/PythonTron/partials/*.handlebars" \
    --template "{BUILDPATH}/factoryabi/PythonTron/contract.handlebars" \
    --language "Python"
echo "==> compile abi to python 🚸✅"
"""

ITEM_TRANSPILE_TS = """
echo "==> 🚸 compile abi to typescript"
if [[ ! -f {outputfolder} ]]; then
    mkdir -p {outputfolder}
fi

abi-gen-uni --abibins "{target_abi}" --out "{outputfolder}" \
    --partials "{BUILDPATH}/factoryabi/TypeScriptTron/partials/*.handlebars" \
    --template "{BUILDPATH}/factoryabi/TypeScriptTron/contract.handlebars" \
    --backend "webtron" \
    --language "TypeScript"

echo "==> compile abi to typescript 🚸✅"
"""
ITEM_TRANSPILE_GO = """
echo "==> 🚸 compile abi to golang"

if [[ ! -f {outputfolder} ]]; then
    mkdir -p {outputfolder}
fi

abigen --abi "{target_abi}" --pkg {classname} --out "{outputfolder}/init.go"

echo "==> compile abi to golang 🚸✅"
"""

PRE_HEAD = """

if ! command -v abi-gen-uni &>/dev/null; then
    echo "abi-gen-uni could not be found"
    cnpm i -g easy-abi-gen;
    exit;   
fi

if ! command -v abigen &>/dev/null; then
    echo "abigen could not be found or implemented. Please install golang abigen";
    exit;
fi



cp -R {FACTORY} {BUILDPATH}/factoryabi 2>/dev/null


"""

SUB_FOOTER = """

rm buildforgebin
rm localpile
rm -rf factoryabi

"""
FORGE_BUILD = """#!/bin/bash

if ! command -v forge &>/dev/null; then
    echo "forge in command is not install. Please visit: https://github.com/foundry-rs/foundry"
    curl -L https://foundry.paradigm.xyz | bash
    exit;
fi
echo "generating compiled files into {BUILD} from {SRC} on forge runs"
forge build --contracts {SRC} --out {BUILD} --optimizer-runs {RUNS} --force

"""