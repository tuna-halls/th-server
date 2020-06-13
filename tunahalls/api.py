import fastapi

app = fastapi.FastAPI()


@app.get("/version")
def version():
    """Just returns the current version"""
    return {"version": "0.1.0-alpha"}
