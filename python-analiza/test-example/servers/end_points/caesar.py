from fastapi import FastAPI


app = FastAPI()

@app.post("/caesar/")
async def caesar_cipher():  
    pass