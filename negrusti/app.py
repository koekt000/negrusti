import uvicorn
from fastapi import Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
import socketio

from db_user_func import get_user_by_email, user_exists, add_new_user

app = FastAPI()

app.mount("/static", StaticFiles(directory="static", html=True), name="static")
sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins="*")

@app.get('/')
def hello_world():
    #return get_file_response("static/html/index.html")
    #return get_file_response("static/html/auth_page.html")
    return get_file_response("static/html/home_page.html")

@app.get("/draw/")
async def get_draw_page() -> FileResponse:
    return get_file_response("static/html/index.html")


@sio.event
async def disconnect(sid):
    print(f"Client {sid} disconnected")


@sio.event
async def connect(sid):
    print(f"Client {sid} connected")


@sio.event
async def draw_event(data):
    await sio.emit('draw_event', data)


def get_file_response(file_path: str) -> FileResponse:
    return FileResponse(file_path)


def get_json_response(content: dict, status_code: int) -> JSONResponse:
    return JSONResponse(content=content, status_code=status_code)


@app.get("/auth/")
async def get_auth_page() -> FileResponse:
    return get_file_response("static/html/auth_page.html")


@app.get("/registration/")
async def get_registration_page() -> FileResponse:
    return get_file_response("static/html/registration.html")


@app.get("/home/")
async def get_registration_page() -> FileResponse:
    return get_file_response("static/html/home_page.html")


@app.get("/login/")
async def get_login_page() -> FileResponse:
    return get_file_response("static/html/login.html")


@app.post("/add_user")
async def create_user(request: Request) -> JSONResponse:
    data = await request.json()

    name = data["name"]
    email = data["email"]
    password = data["password"]

    print(name, email, password)
    if user_exists(email):
        return get_json_response({}, 403)

    add_new_user(name=name, email=email, password=password)

    return get_json_response({}, 200)


@app.post("/find_user")
async def find_user(request: Request) -> JSONResponse:
    data = await request.json()

    email = data["email"]
    password = data["password"]

    if not user_exists(email):
        return get_json_response({}, 404)

    user = get_user_by_email(email=email)
    accepted_response = user.password.password == password
    response_json = {"id": user.id, "accepted": accepted_response}

    return get_json_response(response_json, 200)


@app.websocket("/ws/draw_event")
async def handle_draw_event(websocket: WebSocket):
    await websocket.accept()

    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"draw_event: {data}")
    except Exception as e:
        print(f"WebSocket Error: {e}")


if __name__ == '__main__':
    uvicorn.run('app:app', port=8000, reload=True)

