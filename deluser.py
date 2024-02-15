import inc

inc.cursor.execute("DELETE FROM users WHERE id = ?", (1,))

inc.conn.commit()
inc.conn.close()