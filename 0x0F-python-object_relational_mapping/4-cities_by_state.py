#!/usr/bin/python3
"""cities forigne key"""


if __name__ == '__main__':
    import sys
    import MySQLdb

    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities
                   INNER JOIN states ON states.id=cities.state_id
                   ORDER BY state_id""")
    row = cur.fetchall()
    for i in row:
        print(i)
    cur.close()
    db.close()
