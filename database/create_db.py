import sqlite3


def connect_db():
	conn = sqlite3.connect('database.db')
	cursor = conn.cursor()
	return conn, cursor



def create_movies_tb():
	conn, cursor = connect_db()
	cursor.execute('''
		CREATE TABLE IF NOT EXISTS movies (
			id INTEGER PRIMARY KEY,
			title TEXT,
			description TEXT,
			poster_url TEXT
		)
	''')
	conn.commit()
	conn.close()






