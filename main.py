from fastapi import FastAPI
import uvicorn
class APIContabil(FastAPI):
    def __init__(self, debug = True, title = "APICONTABIL", summary = None
                , description = "API para calculo contabil", version = "0.1.0" ):
        super().__init__(debug=debug, title=title, summary=summary,
                      description=description, version=version)
    

app = APIContabil()
@app.get("/")
async def home_test():
    return {"TESTE":
            "TESTE CONCLUIDO"
            }

if __name__ == '__main__':
    uvicorn.run(app, port=8000)