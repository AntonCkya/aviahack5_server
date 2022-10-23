from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware
from datetime import date, time


from models.buses import Bus, Buses
from models.dispatchers import Dispatcher, Dispatchers
from models.flights import Flight, Flights
from models.queries import Query, Queries


app = FastAPI()
buses = Buses()
disp = Dispatchers()
flights = Flights()
que = Queries()


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
		'position': res[3],
		'name': res[4]
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
			'position': res[3],
			'name': res[4]
			}
			)
	return {"list": l}


@app.get('/get_id_by_token/')
async def get_id_by_token(token: str):
	res = buses.get_id_by_token(token)
	return {
		'id': res[0]
	}

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


# Queries

@app.get('/get_query/')
async def get_query(id: int):
	res = que.get_query(id)
	return {
		'id' : res[0],
		'dispatcher_id' : res[1],
		'flight_id' : res[2],
		'bus_id' : res[3],
		'status' : res[4],
		'begin' : res[5],
		'end' : res[6],
		'start_date' : res[7],
		'start_time' : res[8],
		'end_date' : res[9],
		'end_time' : res[10],
		'passengers_count' : res[11]
	}


@app.post('/post_query/')
async def post_query(q: Query):
	que.post_query(q)
	return {"message": "success"}


@app.delete('/delete_query/')
async def delete_query(id: int):
	que.delete_query(id)
	return {"message": "success"}


@app.get('/get_all_queries_on_bus/')
async def get_all_queries_on_bus(bus_id: int):
	many = que.get_all_queries_on_bus(bus_id)
	l = []
	for res in many:
		l.append(
			{
			'id' : res[0],
			'dispatcher_id' : res[1],
			'flight_id' : res[2],
			'bus_id' : res[3],
			'status' : res[4],
			'begin' : res[5],
			'end' : res[6],
			'start_date' : res[7],
			'start_time' : res[8],
			'end_date' : res[9],
			'end_time' : res[10],
			'passengers_count' : res[11]
			}
			)
	return {"list": l}


@app.put('/put_start_time/')
async def put_start_time (id: int, start_time: str):
	que.put_start_time(id, start_time)
	return {"message": "success"}


@app.put('/put_start_date/')
async def put_start_date (id: int, start_date: date):
	que.put_start_date(id, start_date)
	return {"message": "success"}



@app.put('/put_begin/')
async def put_begin (id: int, begin: int):
	que.put_begin(id, begin)
	return {"message": "success"}



@app.put('/put_end/')
async def put_end (id: int, end: int):
	que.put_end(id, end)
	return {"message": "success"}


@app.get('/get_queries_in_time/')
async def get_queries_in_time(begin_time: str, end_time: str, begin_date: date, end_date: date):
	many = que.get_queries_in_time(begin_time, end_time, begin_date, end_date)
	l = []
	for res in many:
		l.append(
			{
			'id' : res[0],
			'dispatcher_id' : res[1],
			'flight_id' : res[2],
			'bus_id' : res[3],
			'status' : res[4],
			'begin' : res[5],
			'end' : res[6],
			'start_date' : res[7],
			'start_time' : res[8],
			'end_date' : res[9],
			'end_time' : res[10],
			'passengers_count' : res[11]
			}
			)
	return {"list": l}


@app.put('/put_status/')
async def put_status (id: int, status: str):
	que.put_status(id, status)
	return {"message": "success"}


@app.get('/get_all_queries/')
async def get_all_queries():
	many = que.get_all_queries()
	l = []
	for res in many:
		l.append(
			{
			'id' : res[0],
			'dispatcher_id' : res[1],
			'flight_id' : res[2],
			'bus_id' : res[3],
			'status' : res[4],
			'begin' : res[5],
			'end' : res[6],
			'start_date' : res[7],
  			'start_time' : res[8],
 			'passengers_count' : res[9]
			}
			)
	return {"list": l}


@app.put('/put_passengers_count/')
async def put_passengers_count (id: int, passengers_count: str):
	que.put_passengers_count(id, passengers_count)
	return {"message": "success"}


@app.put('/put_end_time/')
async def put_end_time (id: int, end_time: str):
	que.put_end_time(id, end_time)
	return {"message": "success"}


@app.put('/put_end_date/')
async def put_end_date (id: int, end_date: date):
	que.put_end_date(id, end_date)
	return {"message": "success"}


@app.put('/put_bus/')
async def put_bus (id: int, bus_id: int):
	que.put_bus(id, bus_id)
	return {"message": "success"}


@app.put('/put_name_to_bus/')
async def put_name_to_bus (id: int, name: str):
	buses.put_name_to_bus(id, name)
	return {"message": "success"}


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="SVO_bus_API",
        version="1.0",
        description="API for buses and bus dispatchers on Sheremetyevo international airport",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://www.ph4.ru/DL/LOGO/s/sheremetievo.gif"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema
app.openapi = custom_openapi
