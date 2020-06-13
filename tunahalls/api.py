import fastapi

app = fastapi.FastAPI()


@app.get("/version")
def version():
    return {"version": "0.1.0-alpha"}
