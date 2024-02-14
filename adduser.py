import inc

inc.cursor.execute("INSERT INTO users (name) VALUES (?)", ("a man",))

inc.conn.commit()
inc.conn.close()