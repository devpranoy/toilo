import MySQLdb
#+++++++++++++++++++++++ MYSQL Syntax FOR CONNECTION +++++++++++++++++
#db = MySQLdb.connect(host="127.0.0.1",user="root",passwd="0000",db="MINDHACKS")
#cur =db.cursor()
#cur.execute("SELECT * FROM USERS")
#rows = cur.fetchall()
#for row in rows:
#	for col in row:
#		print "%s  " % col
#db.close()

def fetchall(sql):   #function that executes a query and returns its output/ read data from table
    sql = str(sql)
    db = MySQLdb.connect(host="127.0.0.1",user="root",passwd="0000",db="TOILO")
    cur =db.cursor()
    cur.execute(sql)
    info = cur.fetchall()
    db.close()
    return info

def fetchone(sql):   #function that executes a query and returns its output/ read data from table
    sql = str(sql)
    db = MySQLdb.connect(host="127.0.0.1",user="root",passwd="0000",db="TOILO")
    cur =db.cursor()
    cur.execute(sql)
    info = cur.fetchone()
    db.close()
    return info

def inserttodb(sql):    #function to write data to table
    db = MySQLdb.connect(host="127.0.0.1",user="root",passwd="0000",db="TOILO")
    cur =db.cursor()
    cur.execute(sql)
    db.commit()
    db.close()
    return 1
