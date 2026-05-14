from fastapi import FastAPI


app = FastAPI()

@app.post("/hello_endpoint")
def hello():
    return {
        "message": "Hello World",
        "status": "success"
    }
