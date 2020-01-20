# UniVote
Instructions to run this repo are given below.

### What are the current problems in voting?

Government elections around the world are facing increasing security threats and concerns over election integrity.
Although we have moved from paper ballot voting to electronic voting machines (EVMs), they are vulnerable to cyberattacks due to outdated, poorly designed or implemented technology.

Getting people to vote is another significant election challenge. Voter turnout has been declining around the world since the 1990s. There are many reasons for this, including the lack of identification and access to voting booths for voters as well as apathy and mistrust of the political system.   

### How can blockchain help?

#### Transparency
The first benefit that blockchain can bring about is transparency. We know that without transparency, people can become discouraged about the legitimacy of their votes and can lead to questions about tampering and falsified results. This is why it is important that all records are accurate and kept safely. Blockchain and its decentralised ledger can bring about trust at every stage of the voting process.

By using blockchain, votes can be tallied and stored on an immutable public ledger. This means that they can be tracked and counted while being visible to everyone.

#### Security
One of the most important factors of voting is security. Currently, voting systems are very open to hacks. Without substantial security mechanisms in place, malicious actors can enter the system and alter the outcome. This is where blockchain comes in.
All votes could be verified as soon as voting is finished to ensure they are all counted correctly.

#### Anonymity
People want privacy when voting and don’t always want others to know who or what they voted for.
Blockchain allows for anonymity when voting. As with transactions on the blockchain, voters can use their private keys to keep themselves anonymous.

#### Processing Time
Current voting systems often take time to collate and process answers. Often when voting stations are in different areas and offices are not all together, it can be difficult to gather all the information quickly and efficiently. This then leads to time and cost issues.Results can be gathered and processed quickly and straight after the voting has finished.

Refer to the UniVote.pdf for more details about the objectives and working of this application!  


### Implementation of Blockchain

##### Installation of used libraries (on Ubuntu)

~~~
pip3 install flask
pip3 install web3
pip3 install SQLAlchemy (for authentication and database handling for voters, parties etc)
~~~

#### Installation of ganache
Ganache is a personal blockchain for Ethereum development you can use to deploy contracts, develop your applications, and run tests. We used ganache to simulate public and private keys in our ethereum based blockchain application. We used ethereum blockchain because it supports smart contracts.

Download link : https://www.trufflesuite.com/ganache

Installation guide : https://www.codeooze.com/blockchain/ethereum-dev-environment-2019/

#### Steps to run our code
1. Git clone this repository using the command :
```
git clone https://github.com/centerofexcellencehackathon/Team-X
```

2. It will be saved in the directory vote. Change directory using
```
cd vote
```

3. Open another terminal prompt. Change directory to the location where ganache was downloaded. Execute ganache application using the above installation guide before deploying the flask application.  


4. Run the flask application by executing final.py script.
```
python3 final.py
```

4. The flask application will be running on the local server. Open the browser and the application will be running on localhost:5000/. Port number for flask is 5000.

### Note
blockchain.py is a python script by us for understanding how blockchain works on ethereum using ganache. Parts of this has been used in final.py at various code blocks.  

## Future Scope

Authentication using biometric linked to aadhaar number.

BigChain DB for more secure data querying and other database transactions.

Hyperledger instead of ethereum because its more secure.
