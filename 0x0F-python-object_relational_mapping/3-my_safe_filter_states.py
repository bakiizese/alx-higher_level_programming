#!/usr/bin/python3
"""safe from sql injections"""


if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    ms = sys.argv[4]
    cur.execute("""SELECT * FROM states WHERE name LIKE BINARY %s
                ORDER BY states.id""", (ms, ))
    row = cur.fetchall()
    for i in row:
        print(i)
    cur.close()
    db.close()
