from flask_test.DBcm import UseDatabase

dbconfig = {'host': '127.0.0.1',
            'user': 'vsearch',
            'password': 'king_9999',
            'database': 'vsearchlogDB'''}

with UseDatabase(dbconfig) as cursor:
    _SQL='''show tables'''
    cursor.execute(_SQL)
    data=cursor.fetchall()
    print(data)