from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware

from models.buses import Bus, Buses
from models.dispatchers import Dispatcher, Dispatchers


app = FastAPI()
buses = Buses()
disp = Dispatchers()


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
