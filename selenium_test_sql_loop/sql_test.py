import MySQLdb
import sys
from test_mysql_data import PropertyTest

"""
sudo apt-get install python-pip python-dev libmysqlclient-dev
sudo pip install MySQL-python

"""
try:
    db = MySQLdb.connect(
    user = 'root',
    passwd = 'sua_senha',
    host = 'localhost',
    db = 'python_tests'
    )
except Exception as e:
    sys.exit('Ao ao conectar o msyql, verifique as credenciais: '.format(e))

cursor = db.cursor()
cursor.execute('SELECT * FROM users')
result = cursor.fetchall()

# verifica se existe informacao no result
# faz um for com os dados da consulta.
if result:
    for x in result:
        test = PropertyTest()
        test.testProperty(x[1],x[2])
