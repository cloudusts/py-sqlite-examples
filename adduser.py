import inc

inc.cursor.execute("INSERT INTO users (name,password) VALUES (?,?)", ("a man","123456"))

inc.conn.commit()
inc.conn.close()