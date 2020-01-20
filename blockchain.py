from web3 import Web3
import random

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

dict_id={'0x076E4EB4B08eE2AF74A8C27ffBF9E0A4CC0c86c9':'ad3da590851b2bde65b56d77a1b57a8a1cd15f2e9d7d3fa588bfd9682ad7d9cb','0x7836B142b0925f2E4f307d45B05F41594b5CA1Ec':'8e8f7e8d037f98489caf6a8bac8a3dc8795a6c90e6f0d404c54399fbefac592a','0x1CeAfd8B440146212bc86b1FeA70673c56c5A552':'afd7221d3866b2d38fdd62ac4d1f868d421e887cc3dfb9b951a0f44328b83d34'
,'0x87C42f607Abb820049AfEF7482C648670049dE1e':'56de1bc16eb8bacf9b6f7da8422b30823bfac49d94b69303f801e0c95b66d9ad','0x12C8E72f4E6B4a5B49c6AB69687D5fCa425Da545':'49dc005a16997f83b92ed21ef60230dff9483f3d3e12b0772168eb446163e12b','0x54a79C20158B57132d40fc675C2C779BCD1078F0':'99e11feccebd3bdc91cf425bee92c3c3f4bd166a9fa94b5624abf09eb4efe834'}

key=random.choice(list(dict_id.keys()))


voter_1=key
private_key= dict_id[key]

party_a = '0xE0aD2dD9851b60b8FE23827E6aC21018788F95EF' # BJP
party_b = '0x998F8324a9262bFF9Cd5dba0e9679E865b7D8B32' #
party_c = '0x4f541619F081DA24a86826980F4f75fDd40328A0'
party_d = '0x09524678C56B9f7DeE4E8FcA3aBf6f120172c7B3'



nonce = web3.eth.getTransactionCount(voter_1)

#Transaction Details
tx = {
	'nonce': nonce,
	'to': party_a,
	'value': web3.toWei(1, 'ether'),
	'gas': 2000000,
	'gasPrice': 0,
	}


elif n==2:
	nonce = web3.eth.getTransactionCount(voter_1)

#Transaction Details
	tx = {
	'nonce': nonce,
	'to': party_b,
	'value': web3.toWei(1, 'ether'),
	'gas': 2000000,
	'gasPrice': 0,
	}


signed_tx = web3.eth.account.signTransaction(tx, private_key)

tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
curr_hash=web3.toHex(tx_hash)


block_current=web3.eth.getBlock('latest')
block_no=block_current['number']


current_for_timestamp=web3.eth.getBlock(block_no)
time_stamp=current_for_timestamp['timestamp']

print("Block number: ",block_no)
print("Current Hash: ",curr_hash)
print("TimeStamp: ",time_stamp)

if block_current['number']>1:
	prev_block=web3.eth.getTransactionByBlock(block_no-1,0)
	prev_hash=prev_block['hash']
	prev_hash=web3.toHex(prev_hash)
else :
	prev_hash=0

print("Previous Hash: ",prev_hash)

balance_a=web3.eth.getBalance('0xb84E8d8a5f05D28F88cf6d5c50ddB85E737cEbfB')
balance_a=web3.fromWei(balance_a,'ether')

balance_b=web3.eth.getBalance('0x85E5a1Be2736867DDe02Ede2257b118Dd006e8f5')
balance_b=web3.fromWei(balance_b,'ether')


print("Party A :",balance_a-100)
print("Party B :",balance_b-100)
