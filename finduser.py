import inc

inc.cursor.execute("SELECT * FROM users WHERE name = ?", ("a man",))

results = inc.cursor.fetchall()

if results:
    for row in results:
        print(row)
else:
    print("No such user")

inc.conn.close()