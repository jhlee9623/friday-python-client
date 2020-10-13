#!/bin/bash

rm .tmprc

clif keys list > /tmp/list.txt
i=0
while read line
do
    if [[ $line == *"address"* ]];then
        address=$(echo $line | awk -F':' '{print $2}' | sed "s/ //g")
        if [ $i -eq 0 ];then
            echo "export node=$address" >> .tmprc
        else 
            echo "export node$i=$address" >> .tmprc
        fi
        i=$((i+1))
    fi
done < /tmp/list.txt

./make-wallet.py > /tmp/wallet.log

node4=$(cat /tmp/wallet.log | jq .address | sed "s/\"//g")
node4_priv=$(cat /tmp/wallet.log | jq .private_key | sed "s/\"//g")

echo "export node4=$node4" >> .tmprc
echo "export node4_priv=$node4_priv" >> .tmprc

echo "please execute \"source test-scripts/.tmprc\""
