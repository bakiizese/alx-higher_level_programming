#!/usr/bin/python3
"""cities forigne key"""


if __name__ == '__main__':
    import sys
    import MySQLdb

    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    ms = sys.argv[4]
    cur.execute("""SELECT cities.name FROM cities
                   INNER JOIN states ON states.id=cities.state_id WHERE
                   states.name LIKE BINARY %s ORDER BY state_id""", (ms, ))
    rows = cur.fetchall()
    n = 0
    for row in rows:
        print(row[0], end='')
        n += 1
        if n < len(rows):
            print(', ', end='')
    print('')
    cur.close()
    db.close()
