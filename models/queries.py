import sqlite3
from pydantic import BaseModel
from datetime import date, time


class Query(BaseModel):
	dispatcher_id : int
	flight_id : int
	bus_id : int
	status : str
	begin : int
	end : int
	start_date : date
	start_time : str


class Queries:
	"""
	id | dispatcher_id | flight_id | bus_id | status | begin | end | start_date | start_time
	"""
	conn = sqlite3.connect('SVO.db')
	cur = conn.cursor()

	def __init__ (self):
		self.cur.execute("""
					CREATE TABLE IF NOT EXISTS queries
					(
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					dispatcher_id INT NOT NULL,
					flight_id INT NOT NULL,
					bus_id INT NOT NULL,
					status TEXT(1) NOT NULL,
					begin INT NOT NULL,
					end INT NOT NULL,
					start_date DATE NOT NULL,
					start_time TEXT NOT NULL,
					FOREIGN KEY (dispatcher_id) REFERENCES dispatchers (id) ON DELETE RESTRICT ON UPDATE CASCADE,
					FOREIGN KEY (flight_id) REFERENCES flights (id) ON DELETE RESTRICT ON UPDATE CASCADE,
					FOREIGN KEY (bus_id) REFERENCES buses (id) ON DELETE RESTRICT ON UPDATE CASCADE
					);
					""")
		self.conn.commit()


	def post_query (self, q: Query):
		self.cur.execute("""
					INSERT INTO queries (dispatcher_id, flight_id, bus_id, status, begin, end, start_date, start_time)
   					VALUES(?, ?, ?, ?, ?, ?, ?, ?);
   					""", [
   						q.dispatcher_id,
						q.flight_id,
						q.bus_id,
						q.status,
						q.begin,
						q.end,
						q.start_date,
						q.start_time
					])
		self.conn.commit()


	def get_query (self, id: int):
		self.cur.execute("""
					SELECT * 
					FROM queries
					WHERE id = ?;
					""", (id,))
		res = self.cur.fetchone()
		return res


	def delete_query (self, id: int):
		self.cur.execute("""
					DELETE
					FROM queries
					WHERE id = ?;
					""", (id,))
		self.conn.commit()


	def put_start_time (self, id: int, start_time: str):
		self.cur.execute("""
					UPDATE queries
					SET
					start_time = ?
					WHERE id = ?;
					""", [start_time, id])
		self.conn.commit()


	def put_start_date (self, id: int, start_date: date):
		self.cur.execute("""
					UPDATE queries
					SET
					start_date = ?
					WHERE id = ?;
					""", [start_date, id])
		self.conn.commit()
	

	def put_begin (self, id: int, begin: int):
		self.cur.execute("""
					UPDATE queries
					SET
					begin = ?
					WHERE id = ?;
					""", [begin, id])
		self.conn.commit()


	def put_end (self, id: int, end: int):
		self.cur.execute("""
					UPDATE queries
					SET
					end = ?
					WHERE id = ?;
					""", [end, id])
		self.conn.commit()


	def put_bus (self, id: int, bus: int):
		self.cur.execute("""
					UPDATE queries
					SET
					bus_id = ?
					WHERE id = ?;
					""", [bus, id])
		self.conn.commit()


	def get_all_queries_on_bus (self, bus_id: int):
		self.cur.execute("""
					SELECT * 
					FROM queries
					WHERE bus_id = ?;
					""", (bus_id,))
		res = self.cur.fetchall()
		return res


