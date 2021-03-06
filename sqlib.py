import sqlite3
from sqlite3 import Error
import time

table_name = 'ps' + str(int(int(time.time()) / 86400))


def connection(database):
	try:
		con = sqlite3.connect(database)
		return con
	except Error:
		print(Error)


def create_table(con, table_name):
	cursorObj = con.cursor()
	cursorObj.execute(
		"CREATE TABLE if not exists " + table_name + "(id integer PRIMARY KEY AUTOINCREMENT, label text, timestamp integer, percent integer)")
	con.commit()


def listing_table(con):
	listing_table = []
	cursorObj = con.cursor()
	if cursorObj.execute('SELECT name from sqlite_master where type= "table"') == 0:
		print('have no table')
	else:
		for string in cursorObj:
			listing_table.append(string[0])
	return(listing_table)


def insert(con, table_name, data):
	cursorObj = con.cursor()
	create_table(con, table_name)
	#	data = [(label, timestamp, percent)]
	cursorObj.executemany("INSERT INTO " + table_name + " (label, timestamp, percent) VALUES(?, ?, ?)", data)
	con.commit()


def listing_rows(con, table_name):
	listing_row = []
	cursorObj = con.cursor()
	try:
		if not cursorObj.execute('SELECT * FROM ' + table_name):
			print('have no table')
			return([])
		else:
			for string in cursorObj:
				listing_row.append(string)
		return(listing_row)
	except:
		return([])


def del_table(con, table_name):
	cursorObj = con.cursor()
	cursorObj.execute('DROP table if exists ' + table_name)
	con.commit()


def drop_table(con, table_name):
	cursorObj = con.cursor()
	try:
		cursorObj.execute('DROP table if exists ' + table_name)
		con.commit()
		print('table ' + table_name + ' deleted')
	except:
		print('table ' + table_name + ' not deleted')


#con = connection(settings.DATABASE)

#create_table(con, table_name)

#listing_table(con)

#print(listing_rows(con, table_name))

#insert(con, table_name, [('PS0', int(time.time()), int(80))])

#for i in listing_table(con): drop_table(con, i)


#con.close()
