from web3 import Web3
import json
import time

class questionextract():
    ganache_url="HTTP://127.0.0.1:7545"

    web3=Web3(Web3.HTTPProvider(ganache_url))
    print(web3.isConnected())

    web3.eth.defaultAccount=web3.eth.accounts[0]

    abi=json.loads('[{"inputs":[],"name":"createdictionary","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"","type":"string"}],"name":"dictionary","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"randMod","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"nonpayable","type":"function"}]')
    address=web3.toChecksumAddress("0x328f67E06809a2f6bA28BEA5C043e447Ef3BD643")
    contract=web3.eth.contract(address=address,abi=abi)
    contract.functions.createdictionary().call()
    
    x=contract.functions.randMod().call()
    print(x)
    y=contract.functions.randMod().call()
    print(y)
    

