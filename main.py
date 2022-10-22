from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware

from models.buses import Bus, Buses
from models.dispatchers import Dispatcher, Dispatchers
from models.flights import Flight, Flights


app = FastAPI()
buses = Buses()
disp = Dispatchers()
flights = Flights()


origins = [
    "http://localhost"
    "https://localhost",
    "http://localhost:8000",
    "https://localhost:8000",
    "http://localhost:3000",
    "https://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
async def test():
	return {"message": "success"}


# Buses

@app.post('/post_bus/')
async def post_bus(bus: Bus):
	buses.post_bus(bus)
	return {"message": "success"}


@app.delete('/delete_bus/')
async def delete_bus(id: int):
	buses.delete_bus(id)
	return {"message": "success"}


@app.get('/get_bus/')
async def get_bus(id: int):
	res = buses.get_bus(id)
	return {
		'id': res[0],
		'capacity': res[1],
		'token': res[2],
		'position': res[3]
	}


@app.get('/get_all_buses/')
async def get_all_buses():
	many = buses.get_all_buses()
	l = []
	for res in many:
		l.append(
			{
			'id': res[0],
			'capacity': res[1],
			'token': res[2],
			'position': res[3]
			}
			)
	return {"list": l}


# Dispatcher

@app.post('/post_dispatcher/')
async def post_dispatcher(dis: Dispatcher):
	disp.post_dispatcher(dis)
	return {"message": "success"}


@app.delete('/delete_dispatcher/')
async def delete_dispatcher(id: int):
	disp.delete_dispatcher(id)
	return {"message": "success"}


@app.get('/get_dispatcher/')
async def get_dispatcher(id: int):
	res = disp.get_dispatcher(id)
	return {
		'id': res[0],
		'token': res[1],
		'name': res[2]
	}


# Flights

@app.post('/post_flight/')
async def post_flight(flight: Flight):
	flights.post_flight(flight)
	return {"message": "success"}


@app.delete('/delete_flight/')
async def delete_flight(id: int):
	flights.delete_flight(id)
	return {"message": "success"}


@app.get('/get_flight/')
async def get_flight(id: int):
	res = flights.get_flight(id)
	return {
		'id': res[0],
		'date': res[1],
		'AD': res[2],
		'terminal': res[3],
		'ak_code': res[4],
		'flight_number': res[5],
		'time': res[6],
		'ap_code': res[7],
		'aeroport': res[8],
		'BC_type': res[9],
		'parking_place': res[10],
		'gate_number': res[11],
		'passengers_count': res[12]
	}


@app.get('/get_flight_number/')
async def get_flight_number(id: int):
	res = flights.get_flight_number(id)
	return {
		'flight_number': res[0]
	}


@app.get('/get_id_by_flight_number/')
async def get_id_by_flight_number(fln: int):
	res = flights.get_id_by_flight_number(fln)
	return {
		'id': res[0]
	}


@app.put('/put_date_time/')
async def put_date_time(id: int, date: str, time: str):
	flights.put_date_time(id, date, time)
	return {"message": "success"}


@app.put('/put_parking_place/')
async def put_parking_place(id: int, parking_place: int):
	flights.put_parking_place(id, parking_place)
	return {"message": "success"}


@app.put('/put_gate_number/')
async def put_gate_number(id: int, gate_number: str):
	flights.put_gate_number(id, gate_number)
	return {"message": "success"}
