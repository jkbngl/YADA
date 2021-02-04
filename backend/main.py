from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from starlette.middleware.cors import CORSMiddleware

some_file_path = "Tesla reversing sound.mp4"
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/download/")
def main():

    print("test")

    file_like = open(some_file_path, mode="rb")
    return StreamingResponse(file_like, media_type="video/mp4")

