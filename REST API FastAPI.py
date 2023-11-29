from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def hello():
    return {"Hello": "world"}

@app.get('/something')
def Something(): 
    return {"Data": "Something"}

