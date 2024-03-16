# fastapi_neon/main.py


from fastapi import FastAPI

app = FastAPI(title="Hello World API & have great chance to learn micro services with Sir Zia",
              version="0.0.1",
              servers=[
                  {
                      "urls" : "http://0.0.0.0:8000",
                      "description" : "Development Enviornment" 
                  }
              ])
@app.get("/")
def read_root():
    return {"Hello : ""World-GPT-AI"}
