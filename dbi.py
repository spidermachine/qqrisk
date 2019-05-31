#!/usr/bin/python
#  -*- coding: UTF-8 -*-
import sys
import MySQLdb
import os
import datetime

rec_date = datetime.datetime.now().strftime('%Y%m%d')
rec_time = datetime.datetime.now().strftime('%H%M')


def insertTable(user, passwd, db, table, csvfile):
    try:
        conn = getconn(user, db, passwd)
        conn.set_character_set('utf8')
    except Exception as e:
        print ("Error %d: %s" % (e.args[0], e.args[1]))
        sys.exit(1)

    cursor = conn.cursor()
    # cursor.execute('SET NAMES utf8;')
    cursor.execute('SET CHARACTER SET utf8;')
    # cursor.execute('SET character_set_connection=utf8;')
    if os.path.isdir(csvfile):
        files = os.listdir(csvfile)
        for sub_file in files:
            loadcsv(cursor, table, os.path.join(csvfile, sub_file))
    else:
        loadcsv(cursor, table, csvfile)

    # cursor.close()
    conn.commit()
    conn.close()


def insertTableStr(user, passwd, db, table, strList):
    try:
        conn = getconn(user, db, passwd)
        conn.set_character_set('utf8')
    except Exception as e:
        print ("Error %d: %s" % (e.args[0], e.args[1]))
        sys.exit(1)

    cursor = conn.cursor()
    # cursor.execute('SET NAMES utf8;')
    cursor.execute('SET CHARACTER SET utf8;')
    # cursor.execute('SET character_set_connection=utf8;')
    for item in strList:
        numfields = 14
        query = buildInsertCmd(table, numfields)
        vs = item.split(',')[1:]
        vs.insert(1, vs[-1])
        vs = vs[:-1]
        vs.append(rec_date)
        vs.append(rec_time)
        try:
            cursor.execute(query, vs)
        except Exception as e:
            print(e)
    # cursor.close()
    conn.commit()
    conn.close()


def insertTableCodes(user, passwd, db, valList, expired, table='codes'):
    try:
        conn = getconn(user, db, passwd)
        conn.set_character_set('utf8')
    except Exception as e:
        print ("Error %d: %s" % (e.args[0], e.args[1]))
        sys.exit(1)

    cursor = conn.cursor()
    # cursor.execute('SET NAMES utf8;')
    cursor.execute('SET CHARACTER SET utf8;')
    # cursor.execute('SET character_set_connection=utf8;')
    for item in valList:
        numfields = 4
        query = buildInsertCmd(table, numfields)
        vs = list()
        vs.append(rec_date)
        vs.append(item)
        vs.append(expired[0])
        vs.append(expired[1])
        try:
            cursor.execute(query, vs)
        except Exception as e:
            print(e)
    # cursor.close()
    conn.commit()
    conn.close()

def insertTableAlpha(user, passwd, db, valList, table='qqdeltasnapt'):
    try:
        conn = getconn(user, db, passwd)
        conn.set_character_set('utf8')
    except Exception as e:
        print ("Error %d: %s" % (e.args[0], e.args[1]))
        sys.exit(1)

    cursor = conn.cursor()
    # cursor.execute('SET NAMES utf8;')
    cursor.execute('SET CHARACTER SET utf8;')
    # cursor.execute('SET character_set_connection=utf8;')
    for item in valList:
        numfields = 6
        query = buildInsertCmd(table, numfields)
        vs = list()
        vs.append(rec_date)
        vs.append(rec_time)
        for itm in item:
            vs.append(itm)
        try:
            cursor.execute(query, vs)
        except Exception as e:
            print(e)
    # cursor.close()
    conn.commit()
    conn.close()


def selectCodes(user, passwd, db):
    try:
        conn = getconn(user, db, passwd)
        conn.set_character_set('utf8')
    except Exception as e:
        print ("Error %d: %s" % (e.args[0], e.args[1]))
        sys.exit(1)

    cursor = conn.cursor()
    # cursor.execute('SET NAMES utf8;')
    cursor.execute('SET CHARACTER SET utf8;')
    # cursor.execute('SET character_set_connection=utf8;')
    try:
        cursor.execute("select code from codes where rec_date = '{}'".format(rec_date), [])

    except Exception as e:
        print(e)


    data = cursor.fetchall()
    conn.commit()
    conn.close()

    return [dx[0] for dx in data]



def insertTableEtfSnapt(user, passwd, db, valList, table='etfsnapt'):
    try:
        conn = getconn(user, db, passwd)
        conn.set_character_set('utf8')
    except Exception as e:
        print ("Error %d: %s" % (e.args[0], e.args[1]))
        sys.exit(1)

    cursor = conn.cursor()
    # cursor.execute('SET NAMES utf8;')
    cursor.execute('SET CHARACTER SET utf8;')
    # cursor.execute('SET character_set_connection=utf8;')
    numfields = 3
    query = buildInsertCmd(table, numfields)
    vs = list()
    vs.append(rec_date)
    vs.append(rec_time)
    vs.append(valList)
    try:
        cursor.execute(query, vs)
    except Exception as e:
        print(e)
    # cursor.close()
    conn.commit()
    conn.close()


def getconn(user, db, passwd="zxcASDqwe123!@#"):
    conn = MySQLdb.connect(host="192.168.88.129",
                           user=user,
                           passwd=passwd,
                           db=db)
    conn.autocommit(1)
    return conn


def nullify(L):
    """Convert empty strings in the given list to None."""

    # helper function
    def f(x):
        if (x == ""):
            return None
        else:
            return x

    return [f(x) for x in L]


def loadcsv(cursor, table, filename):
    """
    Open a csv file and load it into a sql table.
    Assumptions:
     - the first line in the file is a header
    """

    f = open(filename, encoding='GBK')

    numfields = 10
    query = buildInsertCmd(table, numfields)
    name = None
    code = None
    index = 1
    for line in f.readlines():

        if name is None:
            if index == 1:
                name = line.split(" ")[1].encode('utf8').decode('utf8')
                code = line.split(" ")[0]
        else:
            if index > 2:
                if len(line.split(',')) == 8:
                    vs = list()
                    vs.append(name)
                    vs.append(code)
                    vs.extend(line.replace('\n', '').split(','))
                    try:
                        cursor.execute(query, vs)
                    except Exception as e:
                        print(e)
        index += 1


def buildInsertCmd(table, numfields):
    """
    Create a query string with the given table name and the right
    number of format placeholders.
    example:
    # >>> buildInsertCmd("foo", 3)
    'insert into foo values (%s, %s, %s)' 
    """
    assert (numfields > 0)
    placeholders = (numfields - 1) * "%s, " + "%s"
    query = ("insert into %s" % table) + (" values (%s)" % placeholders)
    return query

