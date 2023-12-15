#!/usr/bin/python3
"""my filter """


if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    nm = sys.argv[4]
    cur.execute(f"SELECT * FROM states WHERE name = '{nm}'\
                  ORDER BY states.id")
    row = cur.fetchall()
    for r in row:
        print(r)
    cur.close()
    db.close()
