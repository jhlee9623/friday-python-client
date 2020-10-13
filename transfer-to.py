#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3

import os
import sys
import requests
import json
from fridaypy import Transaction

host="http://localhost:1317/txs"
privkey=os.environ['node4_priv']
account_num="7"
recipient="friday12e4px0gq573726l4rcey2cne0dvsfypc78veyc"

for i in range(3):
    tx = Transaction(
            privkey=privkey,
            account_num=account_num,
            sequence=i,
            fee=1,
            gas=200000,
            memo="",
            chain_id="testnet",
            sync_mode="async"
        )
    amount = 100
    try:
        tx.add_transfer(recipient=recipient, amount=amount) 
        pushable_tx=tx.get_pushable()
        print(pushable_tx)
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        res=requests.post(host, headers=headers, data=pushable_tx)
        print(res.status_code)
        print(res.text)
        json_res = json.loads(res.text)
        #res=requests.get('/'.join([host, json_res.txhash]))
        #print("query", json_res.txhash, res.text)
    except:
        print("exception happened", sys.exc_info()[0])
