import sqlite3
from pydantic import BaseModel

class Bus(BaseModel):
	capacity : int
	token : str
	position : str


class Buses:
	"""
	id | capacity | token | position
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
					position TEXT NOT NULL
					);
					""")
		self.conn.commit()


	def post_bus (self, bus: Bus):
		self.cur.execute("""
					INSERT INTO buses (capacity, token, position)
   					VALUES(?, ?, ?);
   					""", [bus.capacity, bus.token, bus.position])
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
