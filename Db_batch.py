from final import db, Voter, Constituency, Mla, Party

db.create_all()

constituency_1=Constituency(constituency_name='Badshapur',previous_leader='Tanmay',state_name='Karnataka')
db.session.add(constituency_1)
db.session.commit()

constituency_1=Constituency(constituency_name='Sultanpur',previous_leader='Vedant',state_name='Karnataka')
db.session.add(constituency_1)
db.session.commit()

constituency_1=Constituency(constituency_name='Fazilpur',previous_leader='Karan',state_name='Haryana')
db.session.add(constituency_1)
db.session.commit()

constituency_1=Constituency(constituency_name='Faridabad',previous_leader='Saurabh',state_name='Gujarat')
db.session.add(constituency_1)
db.session.commit()




party_1=Party(party_id='123456',party_name='BJP',party_leader='Tanmay')
db.session.add(party_1)
db.session.commit()

party_1=Party(party_id='111111',party_name='INC',party_leader='Patil')
db.session.add(party_1)
db.session.commit()

party_1=Party(party_id='987654',party_name='NationalistCongress',party_leader='Alok')
db.session.add(party_1)
db.session.commit()

party_1=Party(party_id='999999',party_name='ShivSena',party_leader='Prasad')
db.session.add(party_1)
db.session.commit()




mla_1=Mla(mla_id='333999',mla_name='Yashwardhan',mla_dob='10/10/1970',mla_sex='M',party_id='111111',mla_constituency='Faridabad')
db.session.add(mla_1)
db.session.commit()

mla_1=Mla(mla_id='112233',mla_name='Rahul',mla_dob='11/02/1980',mla_sex='M',party_id='111111',mla_constituency='Fazilpur')
db.session.add(mla_1)
db.session.commit()

mla_1=Mla(mla_id='998877',mla_name='Rishika',mla_dob='09/10/2000',mla_sex='F',party_id='987654',mla_constituency='Faridabad')
db.session.add(mla_1)
db.session.commit()

mla_1=Mla(mla_id='135790',mla_name='Ashok',mla_dob='31/01/1969',mla_sex='M',party_id='999999',mla_constituency='Badshapur')
db.session.add(mla_1)
db.session.commit()

mla_1=Mla(mla_id='086413',mla_name='Kritika',mla_dob='29/02/1995',mla_sex='F',party_id='123456',mla_constituency='Sultanpur')
db.session.add(mla_1)
db.session.commit()

mla_1=Mla(mla_id='334445',mla_name='Yadav',mla_dob='01/01/1930',mla_sex='M',party_id='111111',mla_constituency='Sultanpur')
db.session.add(mla_1)
db.session.commit()

mla_1=Mla(mla_id='223344',mla_name='Mahi',mla_dob='15/12/1972',mla_sex='F',party_id='999999',mla_constituency='Faridabad')
db.session.add(mla_1)
db.session.commit()

mla_1=Mla(mla_id='998866',mla_name='Kohli',mla_dob='11/05/1962',mla_sex='M',party_id='999999',mla_constituency='Fazilpur')
db.session.add(mla_1)
db.session.commit()

mla_1=Mla(mla_id='345677',mla_name='Vayu',mla_dob='11/02/1989',mla_sex='M',party_id='999999',mla_constituency='Fazilpur')
db.session.add(mla_1)
db.session.commit()

mla_1=Mla(mla_id='777777',mla_name='Vedi',mla_dob='10/06/1999',mla_sex='F',party_id='111111',mla_constituency='Badshapur')
db.session.add(mla_1)
db.session.commit()




