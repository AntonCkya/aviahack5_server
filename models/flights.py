import sqlite3
from pydantic import BaseModel
from datetime import date, time


class Flight (BaseModel):
	date: date
	AD: str
	terminal: str 
	ak_code: str 
	flight_number: int 
	time: str
	ap_code: str 
	aeroport: str
	BC_type: str
	parking_place: int
	gate_number: str
	passengers_count: int


class Flights:
	"""
	id | date | AD | terminal | ak_code | flight_number | time | ap_code | aeroport | BC_type |
	| parking_place | gate_number | passengers_count
	"""
	conn = sqlite3.connect('SVO.db')
	cur = conn.cursor()

	def __init__ (self):
		self.cur.execute("""
					CREATE TABLE IF NOT EXISTS flights
					(
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					date DATE NOT NULL,
					AD TEXT(1) NOT NULL,
					terminal TEXT NOT NULL,
					ak_code TEXT NOT NULL,
					flight_number INT NOT NULL,
					time TEXT NOT NULL,
					ap_code TEXT NOT NULL,
					aeroport TEXT NOT NULL,
					BC_type TEXT NOT NULL,
					parking_place INT NOT NULL,
					gate_number TEXT(5) NOT NULL,
					passengers_count INT NOT NULL
					);
					""")
		self.conn.commit()


	def post_flight (self, fl: Flight):
		self.cur.execute("""
					INSERT INTO flights (date, AD, terminal, ak_code, flight_number, time, ap_code, aeroport, BC_type, parking_place, gate_number, passengers_count)
   					VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
   					""", [
   						fl.date,
						fl.AD,
						fl.terminal,
						fl.ak_code,
						fl.flight_number,
						fl.time,
						fl.ap_code,
						fl.aeroport,
						fl.BC_type,
						fl.parking_place,
						fl.gate_number,
						fl.passengers_count
   					])
		self.conn.commit()


	def delete_flight (self, id: int):
		self.cur.execute("""
					DELETE
					FROM flights
					WHERE id = ?;
					""", (id,))
		self.conn.commit()


	def get_flight (self, id: int):
		self.cur.execute("""
					SELECT * 
					FROM flights
					WHERE id = ?;
					""", (id,))
		res = self.cur.fetchone()
		return res


	def get_flight_number (self, id: int):
		self.cur.execute("""
					SELECT flight_number 
					FROM flights
					WHERE id = ?;
					""", (id,))
		res = self.cur.fetchone()
		return res


	def get_id_by_flight_number (self, fln: int):
		self.cur.execute("""
					SELECT id 
					FROM flights
					WHERE flight_number = ?;
					""", (fln,))
		res = self.cur.fetchone()
		return res


	def put_date_time (self, id: int, date:str, time: str):
		self.cur.execute("""
					UPDATE flights
					SET
					date = ?,
					time = ?
					WHERE id = ?;
					""", [date, time, id])
		self.conn.commit()


	def put_parking_place (self, id: int, parking_place: int):
		self.cur.execute("""
					UPDATE flights
					SET
					parking_place = ?
					WHERE id = ?;
					""", [parking_place, id])
		self.conn.commit()


	def put_gate_number (self, id: int, gate_number: str):
		self.cur.execute("""
					UPDATE flights
					SET
					gate_number = ?
					WHERE id = ?;
					""", [gate_number, id])
		self.conn.commit()