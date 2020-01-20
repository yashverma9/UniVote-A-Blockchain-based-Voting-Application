from flask import Flask, render_template, url_for, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from datetime import datetime
from web3 import Web3
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e36106119a10a327dd4fd993dfad8262'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  #3 forward slashes for relative path sqlite for easy deployment of database
db = SQLAlchemy(app)  #Create a database instance
ganache_url = "http://127.0.0.1:7545"	
web3 = Web3(Web3.HTTPProvider(ganache_url))



#Blochain implementation

voter_1 = '0x076E4EB4B08eE2AF74A8C27ffBF9E0A4CC0c86c9' #Voter
party_a = '0xE0aD2dD9851b60b8FE23827E6aC21018788F95EF' # BJP
party_b = '0x998F8324a9262bFF9Cd5dba0e9679E865b7D8B32' # CONG
party_c = '0x4f541619F081DA24a86826980F4f75fDd40328A0' # RSC
party_d = '0x09524678C56B9f7DeE4E8FcA3aBf6f120172c7B3' #SHIV SENA

private_key='56de1bc16eb8bacf9b6f7da8422b30823bfac49d94b69303f801e0c95b66d9ad'


#Tables
class Voter(db.Model):
	voter_id=db.Column(db.String(10),primary_key=True)
	voter_name=db.Column(db.String(20))
	region=db.Column(db.String(20),db.ForeignKey('constituency.constituency_name'))
	voter_dob=db.Column(db.String(10),nullable=False)
	voter_sex=db.Column(db.String(1),nullable=False)
	voter_pin=db.Column(db.String(10), nullable=False)	

	def __repr__(self):
		return "{},{},{},{},{},{}".format(self.voter_id,self.voter_name,self.region,self.voter_dob,self.voter_sex,self.voter_pin)

class Mla(db.Model):
	mla_id=db.Column(db.String(10),primary_key=True)
	mla_name=db.Column(db.String(20))
	mla_dob=db.Column(db.String(10),nullable=False)
	mla_sex=db.Column(db.String(1),nullable=False)
	party_id=db.Column(db.String(10),db.ForeignKey('party.party_id'))
	mla_constituency=db.Column(db.String(20),db.ForeignKey('constituency.constituency_name')) 

	def __repr__(self):
		return "{},{},{},{}{}".format(self.mla_id,self.mla_name,self.mla_age,self.mla_sex,self.party,self.mla_constituency)

class Constituency(db.Model):
	constituency_name=db.Column(db.String(20),primary_key=True)
	previous_leader=db.Column(db.String(20))
	state_name=db.Column(db.String(20))
	belongs_to=db.relationship('Voter',backref='constituency',lazy=True)
	contesting_from=db.relationship('Mla',backref='constituency',lazy=True)

	def __repr__(self):
		return "{},{},{}".format(self.constituency_name,self.previous_leader,self.state_name)

class Party(db.Model):
	party_id=db.Column(db.String(10),primary_key=True)
	party_name=db.Column(db.String(20))
	party_leader=db.Column(db.String(20))
	works_for=db.relationship('Mla',backref='party',lazy=True)

	def __repr__(self):
		return "{},{},{}".format(self.party_id,self.party_name,self.party_leader)



#Routes

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/voterHome')
def voterHome():
	return render_template('voterHome.html')


@app.route('/leader')
def leader():
	with open("voter.txt", "r") as f:
		region1 = f.readline()
	
	sql=text('select constituency_name,state_name,previous_leader,mla_name,mla_dob,mla_sex,party_name,party_leader from voter,constituency,mla,party where region=constituency_name and mla_constituency=constituency_name and mla.party_id = party.party_id and constituency_name = :reg')
	#sql = text('select * from mla')

	result=db.engine.execute(sql, reg=region1)
	res = list(result)
	return render_template('leader.html', res=res)



@app.route('/login')
def login():
	return render_template('index.html')

@app.route('/login',methods=['POST'])
def login_post():
	voter_id=request.form.get('voter_id')
	voter_pin=request.form.get('voter_pin')

	voter=Voter.query.filter_by(voter_id=voter_id).first()
	if not voter or (str(voter.voter_pin)!=str(voter_pin)):
		flash('SORRY! Please check your details and try again.')
		return redirect(url_for('login'))

	with open("voter.txt", "w+") as f:
		f.write(str(voter.region))

	flash('Successful login!')
	return redirect(url_for('voterHome'))



@app.route('/register')
def register():
	return render_template('register.html')


@app.route('/register',methods=['POST'])
def register_post():
	voter_id = request.form.get('voter_id')
	voter_name = request.form.get('voter_name')
	dob = request.form.get('dob')
	voter_sex = request.form.get('sex')
	voter_pin= request.form.get('voter_pin')
	region=request.form.get('region')

	voter = Voter.query.filter_by(voter_id=voter_id).first()
	if voter:
		flash('Voter already exists in Database!')
		return redirect(url_for('login'))

	voter_1=Voter(voter_id=voter_id,voter_name=voter_name,region=region,voter_dob=dob,voter_sex=voter_sex,voter_pin=voter_pin)
	db.session.add(voter_1)
	db.session.commit()

	return redirect(url_for('login'))


@app.route('/admin')
def admin():
	return render_template('indexAdmin.html')

@app.route('/admin', methods=['POST'])
def admin_post():
	admin_pin = request.form.get('admin_pin')
	if admin_pin=='qwerty':
		return redirect(url_for('adminHome'))	
	return render_template('indexAdmin.html')


@app.route('/adminHome')
def adminHome():
	return render_template('adminHome.html')



@app.route('/result1')
def result1():
	sql_1=text('select * from voter')
	result=db.engine.execute(sql_1)
	res=list(result)
	return render_template('result1.html',res=res)

@app.route('/result2')
def result2():
	sql_2=text('select * from party')
	result=db.engine.execute(sql_2)
	res=list(result)
	return render_template('result2.html',res=res)

@app.route('/result3')
def result3():
	sql_3= text('select mla_id, mla_name, mla_dob, mla_sex, party_name, mla_constituency from mla, party where mla.party_id=party.party_id')
	result=db.engine.execute(sql_3)
	res=list(result)
	return render_template('result3.html',res=res)


@app.route('/result4')
def result4():
	return render_template('result4.html')


@app.route('/result4',methods=['POST'])
def result4Post():
	party1 = request.form.get('partyName')
	sql_4=text('select mla_id,mla_name,mla_dob,mla_sex,mla_constituency from mla,party where mla.party_id=party.party_id and party_name =:par')
	result=db.engine.execute(sql_4,par=party1)
	res=list(result)
	return render_template('result4.html', res=res)



@app.route('/result5')
def result5():
	return render_template('result5.html')

@app.route('/result5', methods=['POST'])
def result5Post():
	constituency1 = request.form.get('constituency_name')
	sql_5=text('select mla_id,mla_name,mla_dob,mla_sex,party_name from mla,constituency,party where mla_constituency=constituency_name and mla.party_id = party.party_id and mla_constituency = :const')	
	result=db.engine.execute(sql_5,const=constituency1)
	res=list(result)
	return render_template('result5.html', res=res)



@app.route('/voting')
def voting():
	return render_template('clist.html')


@app.route('/partya')
def partya():

	dict_id={'0x076E4EB4B08eE2AF74A8C27ffBF9E0A4CC0c86c9':'ad3da590851b2bde65b56d77a1b57a8a1cd15f2e9d7d3fa588bfd9682ad7d9cb','0x7836B142b0925f2E4f307d45B05F41594b5CA1Ec':'8e8f7e8d037f98489caf6a8bac8a3dc8795a6c90e6f0d404c54399fbefac592a','0x1CeAfd8B440146212bc86b1FeA70673c56c5A552':'afd7221d3866b2d38fdd62ac4d1f868d421e887cc3dfb9b951a0f44328b83d34'
	,'0x87C42f607Abb820049AfEF7482C648670049dE1e':'56de1bc16eb8bacf9b6f7da8422b30823bfac49d94b69303f801e0c95b66d9ad','0x12C8E72f4E6B4a5B49c6AB69687D5fCa425Da545':'49dc005a16997f83b92ed21ef60230dff9483f3d3e12b0772168eb446163e12b','0x54a79C20158B57132d40fc675C2C779BCD1078F0':'99e11feccebd3bdc91cf425bee92c3c3f4bd166a9fa94b5624abf09eb4efe834'}

	key=random.choice(list(dict_id.keys()))
	voter_1=key
	private_key= dict_id[key]
	nonce = web3.eth.getTransactionCount(voter_1)
	tx={'nonce':nonce,	'to':party_a, 'value':web3.toWei(1, 'ether'),'gas':2000000, 'gasPrice':0}
	signed_tx = web3.eth.account.signTransaction(tx, private_key)

	tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
	curr_hash=web3.toHex(tx_hash) #To print


	block_current=web3.eth.getBlock('latest')
	block_no=block_current['number'] #To print


	current_for_timestamp=web3.eth.getBlock(block_no)
	time_stamp=current_for_timestamp['timestamp'] # To print
	
	if block_current['number']>1:
		prev_block=web3.eth.getTransactionByBlock(block_no-1,0)
		prev_hash=prev_block['hash']
		prev_hash=web3.toHex(prev_hash)# To print
	else :
		prev_hash=0 #or this to Print
	balance_a=web3.eth.getBalance(party_a)
	balance_a=web3.fromWei(balance_a,'ether') #To print
	balance_a-=100
	#cnt_a = balance_a
	'''
	cnt_a = count_a(count=balance_a)
	db.Session.add(cnt_a)
	db.Session.commit()
	'''

	with open("a.txt", "w+") as f:
		f.write(str(balance_a))

	return render_template('party_a.html',curr_hash=curr_hash,block_no=block_no,time_stamp=time_stamp,prev_hash=prev_hash,balance_a=balance_a)






@app.route('/partyb')
def partyb():

	dict_id={'0x076E4EB4B08eE2AF74A8C27ffBF9E0A4CC0c86c9':'ad3da590851b2bde65b56d77a1b57a8a1cd15f2e9d7d3fa588bfd9682ad7d9cb','0x7836B142b0925f2E4f307d45B05F41594b5CA1Ec':'8e8f7e8d037f98489caf6a8bac8a3dc8795a6c90e6f0d404c54399fbefac592a','0x1CeAfd8B440146212bc86b1FeA70673c56c5A552':'afd7221d3866b2d38fdd62ac4d1f868d421e887cc3dfb9b951a0f44328b83d34'
	,'0x87C42f607Abb820049AfEF7482C648670049dE1e':'56de1bc16eb8bacf9b6f7da8422b30823bfac49d94b69303f801e0c95b66d9ad','0x12C8E72f4E6B4a5B49c6AB69687D5fCa425Da545':'49dc005a16997f83b92ed21ef60230dff9483f3d3e12b0772168eb446163e12b','0x54a79C20158B57132d40fc675C2C779BCD1078F0':'99e11feccebd3bdc91cf425bee92c3c3f4bd166a9fa94b5624abf09eb4efe834'}

	key=random.choice(list(dict_id.keys()))
	voter_1=key
	private_key= dict_id[key]
	nonce = web3.eth.getTransactionCount(voter_1)
	tx={'nonce':nonce,	'to':party_b, 'value':web3.toWei(1, 'ether'),'gas':2000000, 'gasPrice':0}
	signed_tx = web3.eth.account.signTransaction(tx, private_key)

	tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
	curr_hash=web3.toHex(tx_hash) #To print


	block_current=web3.eth.getBlock('latest')
	block_no=block_current['number'] #To print


	current_for_timestamp=web3.eth.getBlock(block_no)
	time_stamp=current_for_timestamp['timestamp'] # To print
	
	if block_current['number']>1:
		prev_block=web3.eth.getTransactionByBlock(block_no-1,0)
		prev_hash=prev_block['hash']
		prev_hash=web3.toHex(prev_hash)# To print
	else :
		prev_hash=0 #or this to Print
	balance_b=web3.eth.getBalance(party_b)
	balance_b=web3.fromWei(balance_b,'ether') #To print
	balance_b-=100

	with open("b.txt", "w+") as f:
		f.write(str(balance_b))

	#cnt_b = balance_b
	return render_template('party_b.html',curr_hash=curr_hash,block_no=block_no,time_stamp=time_stamp,prev_hash=prev_hash,balance_b=balance_b)




@app.route('/partyc')
def partyc():

	dict_id={'0x076E4EB4B08eE2AF74A8C27ffBF9E0A4CC0c86c9':'ad3da590851b2bde65b56d77a1b57a8a1cd15f2e9d7d3fa588bfd9682ad7d9cb','0x7836B142b0925f2E4f307d45B05F41594b5CA1Ec':'8e8f7e8d037f98489caf6a8bac8a3dc8795a6c90e6f0d404c54399fbefac592a','0x1CeAfd8B440146212bc86b1FeA70673c56c5A552':'afd7221d3866b2d38fdd62ac4d1f868d421e887cc3dfb9b951a0f44328b83d34'
	,'0x87C42f607Abb820049AfEF7482C648670049dE1e':'56de1bc16eb8bacf9b6f7da8422b30823bfac49d94b69303f801e0c95b66d9ad','0x12C8E72f4E6B4a5B49c6AB69687D5fCa425Da545':'49dc005a16997f83b92ed21ef60230dff9483f3d3e12b0772168eb446163e12b','0x54a79C20158B57132d40fc675C2C779BCD1078F0':'99e11feccebd3bdc91cf425bee92c3c3f4bd166a9fa94b5624abf09eb4efe834'}

	key=random.choice(list(dict_id.keys()))
	voter_1=key
	private_key= dict_id[key]
	nonce = web3.eth.getTransactionCount(voter_1)
	tx={'nonce':nonce,	'to':party_c, 'value':web3.toWei(1, 'ether'),'gas':2000000, 'gasPrice':0}
	signed_tx = web3.eth.account.signTransaction(tx, private_key)

	tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
	curr_hash=web3.toHex(tx_hash) #To print


	block_current=web3.eth.getBlock('latest')
	block_no=block_current['number'] #To print


	current_for_timestamp=web3.eth.getBlock(block_no)
	time_stamp=current_for_timestamp['timestamp'] # To print
	
	if block_current['number']>1:
		prev_block=web3.eth.getTransactionByBlock(block_no-1,0)
		prev_hash=prev_block['hash']
		prev_hash=web3.toHex(prev_hash)# To print
	else :
		prev_hash=0 #or this to Print
	balance_c=web3.eth.getBalance(party_c)
	balance_c=web3.fromWei(balance_c,'ether') #To print
	balance_c-=100
	#cnt_c = balance_c
	with open("c.txt", "w+") as f:
		f.write(str(balance_c))
	return render_template('party_c.html',curr_hash=curr_hash,block_no=block_no,time_stamp=time_stamp,prev_hash=prev_hash,balance_c=balance_c)





@app.route('/partyd')
def partyd():

	dict_id={'0x076E4EB4B08eE2AF74A8C27ffBF9E0A4CC0c86c9':'ad3da590851b2bde65b56d77a1b57a8a1cd15f2e9d7d3fa588bfd9682ad7d9cb','0x7836B142b0925f2E4f307d45B05F41594b5CA1Ec':'8e8f7e8d037f98489caf6a8bac8a3dc8795a6c90e6f0d404c54399fbefac592a','0x1CeAfd8B440146212bc86b1FeA70673c56c5A552':'afd7221d3866b2d38fdd62ac4d1f868d421e887cc3dfb9b951a0f44328b83d34'
	,'0x87C42f607Abb820049AfEF7482C648670049dE1e':'56de1bc16eb8bacf9b6f7da8422b30823bfac49d94b69303f801e0c95b66d9ad','0x12C8E72f4E6B4a5B49c6AB69687D5fCa425Da545':'49dc005a16997f83b92ed21ef60230dff9483f3d3e12b0772168eb446163e12b','0x54a79C20158B57132d40fc675C2C779BCD1078F0':'99e11feccebd3bdc91cf425bee92c3c3f4bd166a9fa94b5624abf09eb4efe834'}

	key=random.choice(list(dict_id.keys()))
	voter_1=key
	private_key= dict_id[key]
	nonce = web3.eth.getTransactionCount(voter_1)
	tx={'nonce':nonce,	'to':party_d, 'value':web3.toWei(1, 'ether'),'gas':2000000, 'gasPrice':0}
	signed_tx = web3.eth.account.signTransaction(tx, private_key)

	tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
	curr_hash=web3.toHex(tx_hash) #To print


	block_current=web3.eth.getBlock('latest')
	block_no=block_current['number'] #To print


	current_for_timestamp=web3.eth.getBlock(block_no)
	time_stamp=current_for_timestamp['timestamp'] # To print
	
	if block_current['number']>1:
		prev_block=web3.eth.getTransactionByBlock(block_no-1,0)
		prev_hash=prev_block['hash']
		prev_hash=web3.toHex(prev_hash)# To print
	else :
		prev_hash=0 #or this to Print
	balance_d=web3.eth.getBalance(party_d)
	balance_d=web3.fromWei(balance_d,'ether') #To print
	balance_d-=100
	#cnt_d=balance_d
	with open("d.txt", "w+") as f:
		f.write(str(balance_d))
	return render_template('party_d.html',curr_hash=curr_hash,block_no=block_no,time_stamp=time_stamp,prev_hash=prev_hash,balance_d=balance_d)


@app.route('/results')
def res():
	with open("a.txt", "r") as f:
		cnt_a = f.readline() 
		cnt_a = int(cnt_a)
	with open("b.txt", "r") as f:
		cnt_b = f.readline() 
		cnt_b = int(cnt_b)
	with open("c.txt", "r") as f:
		cnt_c = f.readline() 
		cnt_c = int(cnt_c)
	with open("d.txt", "r") as f:
		cnt_d = f.readline() 
		cnt_d = int(cnt_d)
	return render_template('results.html', cnt_a=cnt_a, cnt_b=cnt_b, cnt_c=cnt_c, cnt_d=cnt_d)


if __name__ == '__main__':
	app.run(debug=True)
