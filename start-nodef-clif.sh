#!/bin/bash

nodef start 2>&1 | tee /tmp/nodef.log &
sleep 20
clif rest-server --chain-id=testnet --laddr tcp://0.0.0.0:1317 2>&1 > /tmp/clif.log
