from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Home Page</title>
    </head>
    <body>
        <h1>Welcome to My FastAPI Server</h1>
        <p>This is the home page of the server.</p>
        <p>You can navigate to other pages or APIs from here.</p>
    </body>
    </html>
    """
@app.get("/fhtrust.yaml")
async def get_yaml():
    file_path = "fhtrust.yaml"
    if os.path.isfile(file_path):
        return FileResponse(file_path, media_type='application/yaml')
    else:
        raise HTTPException(status_code=404, detail="File not found")

@app.get("/plugin.json")
async def get_json():
    file_path = "plugin.json"
    if os.path.isfile(file_path):
        return FileResponse(file_path, media_type='application/json')
    else:
        raise HTTPException(status_code=404, detail="File not found")
