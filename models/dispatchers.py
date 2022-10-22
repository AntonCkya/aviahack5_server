import sqlite3
from pydantic import BaseModel

class Dispatcher (BaseModel):
	token: str
	name: str


class Dispatchers:
	"""
	id | token | name 
	"""
	conn = sqlite3.connect('SVO.db')
	cur = conn.cursor()

	def __init__ (self):
		self.cur.execute("""
					CREATE TABLE IF NOT EXISTS dispatchers
					(
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					token TEXT,
					name TEXT NOT NULL
					);
					""")
		self.conn.commit()


	def get_dispatcher(self, id: int):
		self.cur.execute("""
					SELECT * 
					FROM dispatchers
					WHERE id = ?;
					""", (id,))
		res = self.cur.fetchone()
		return res


	def post_dispatcher (self, dis: Dispatcher):
		self.cur.execute("""
					INSERT INTO dispatchers (token, name)
   					VALUES(?, ?);
   					""", [dis.token, dis.name])
		self.conn.commit()


	def delete_dispatcher (self, id: int):
		self.cur.execute("""
					DELETE
					FROM dispatcher
					WHERE id = ?;
					""", (id,))
		self.conn.commit()
