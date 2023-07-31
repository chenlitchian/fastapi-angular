from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
# Create a FastAPI instance
app = FastAPI()
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
import os
pid = os.getpid()
from a2wsgi import WSGIMiddleware, ASGIMiddleware
import uvicorn
import gunicorn

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


# Get the absolute path to the "dist" directory
dist_path = Path(__file__).parent / "dist"

# Mount the "dist" directory to serve static files
app.mount("/static", StaticFiles(directory=str(dist_path)), name="static")


# Initialize Jinja2Templates to render the index.html file
templates = Jinja2Templates(directory=str(dist_path))


# Define another route
# @app.get("/items/{item_id}")
# @limiter.limit("10/minute")
# def read_item(request: Request, item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q, "pid":pid}
@app.get("/")
def root():
    a = "a"
    b = "b" + a
    return {"hello world": b}


# @app.get("/", response_class=HTMLResponse)
# async def read_root(request: Request):
#     # Render the index.html file using Jinja2Templates
#     return templates.TemplateResponse("index.html", {"request": request})


# Custom route to serve specific file extensions (.css and .js)
# @app.get("/{file_path:path}")
# async def serve_static_file(file_path: str, request: Request):
#     # Get the file extension from the requested URL path
#     file_extension = Path(file_path).suffix
#      # Define the list of allowed file extensions to serve
#     allowed_extensions = {".css", ".js", ".png", ".jpg", ".jpeg", ".gif", ".svg"}

#     # Check if the file extension is in the allowed_extensions set
#     if file_extension in allowed_extensions:
#         # Get the absolute path to the requested file
#         file_path = dist_path / file_path

#         # Check if the file exists, and if so, return it
#         if file_path.exists():
#             return FileResponse(file_path)

#     # Return a 404 Not Found response if the file is not found
#     return templates.TemplateResponse("index.html", {"request": request})

# # Define a route
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# wsgi_app = ASGIMiddleware(app)



# if __name__ == "__main__":
#     gunicorn.run(wsgi_app, host="0.0.0.0", port=8000)



