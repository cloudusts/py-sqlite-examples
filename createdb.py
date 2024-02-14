import inc

inc.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)''')

inc.conn.commit()
inc.conn.close()