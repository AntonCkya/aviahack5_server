import sqlite3
from pydantic import BaseModel


class Bus(BaseModel):
	capacity : int
	token : str
	position : str
	name: str


class Buses:
	"""
	id | capacity | token | position | name
	"""
	conn = sqlite3.connect('SVO.db')
	cur = conn.cursor()

	def __init__ (self):
		self.cur.execute("""
					CREATE TABLE IF NOT EXISTS buses
					(
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					capacity INT NOT NULL,
					token TEXT,
					position TEXT NOT NULL,
					name TEXT
					);
					""")
		self.conn.commit()


	def post_bus (self, bus: Bus):
		self.cur.execute("""
					INSERT INTO buses (capacity, token, position, name)
   					VALUES(?, ?, ?, ?);
   					""", [bus.capacity, bus.token, bus.position, bus.name])
		self.conn.commit()


	def delete_bus (self, id: int):
		self.cur.execute("""
					DELETE
					FROM buses
					WHERE id = ?;
					""", (id,))
		self.conn.commit()



	def get_bus (self, id: int):
		self.cur.execute("""
					SELECT * 
					FROM buses
					WHERE id = ?;
					""", (id,))
		res = self.cur.fetchone()
		return res


	def get_all_buses (self):
		self.cur.execute("""
					SELECT * 
					FROM buses;
					""")
		res = self.cur.fetchall()
		return res


	def get_id_by_token (self, token: str):
		self.cur.execute("""
					SELECT id 
					FROM buses
					WHERE token LIKE ?;
					""", (token,))
		res = self.cur.fetchone()
		return res


	def put_name_to_bus (self, id: int, name: str):
		self.cur.execute("""
					UPDATE buses
					SET
					name = ?
					WHERE id = ?;
					""", [name, id])
		self.conn.commit()
