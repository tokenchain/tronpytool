# !/usr/bin/env python
# coding: utf-8
import logging

from deploy import WrapDeploy

sol_compile = False
deploynew = False
testContracts = False
debugAll = False

if debugAll:
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
    logger = logging.getLogger()


ws = WrapDeploy().connect_deploy(sol_compile, deploynew)

ws.deploy_BonusKeep()
ws.deploy_MasonicCoal()

if testContracts:
    ws.init_test_query()

ws.after_deployment_initialize_settings()
