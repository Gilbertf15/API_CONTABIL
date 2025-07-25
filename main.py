from fastapi import FastAPI, Request
import uvicorn
import requests
from app.api.routes.routes import routercontabil
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from  fastapi.templating import Jinja2Templates

class APIContabil(FastAPI):
    def __init__(self, debug = True, title = "APICONTABIL", summary = None
                , description = "API para calculo contabil", version = "0.1.0" ):
        super().__init__(debug=debug, title=title, summary=summary,
                      description=description, version=version)

class IncludeRoutes:
    @staticmethod
    def main_include_routes(app:FastAPI):
        app.include_router(routercontabil)

app = APIContabil()

app.mount("/app/frontend/static", StaticFiles(directory="app/frontend/static"), name="static")
templates = Jinja2Templates(directory="app/frontend/templates")

@app.get("/", response_class=HTMLResponse)
async def home_test(request: Request):
    
    return templates.TemplateResponse("home.html", {'request': request})
    """except requests.exceptions.HTTPError:
        return {
            "ERROR": "Error API"
        }
    
    except requests.exceptions.ConnectionError:
        return {
           "ERROR":  "Error connection"
        }"""
IncludeRoutes.main_include_routes(app)
if __name__ == '__main__':
    uvicorn.run(app, port=8000)