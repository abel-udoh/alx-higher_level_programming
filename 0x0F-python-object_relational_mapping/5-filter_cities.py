#!/usr/bin/python3

"""
a script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )

    cur = db.cursor()
    inquiry = """SELECT name FROM cities
    WHERE state_id = (SELECT id FROM states WHERE name = %s)
    ORDER BY id ASC"""
    cur.execute(inquiry, (sys.argv[4],))
    output = cur.fetchall()

    inquiry_list = []
    for row in output:
        inquiry_list.append(row[0])
    print(", ".join(inquiry_list))

    cur.close()

    db.close()
