from fastapi import FastAPI


app = FastAPI()


"""
GET /test
Response: { “msg”: “hi from test”}
תיאור: נקודת קצה בסיסית לצורך בדיקות.
"""


@app.get("/test/")
def test_endpoint():  
    return {"msg": "hi from test"}

"""
GET /test/:name
Response: { “msg”: “saved user”}
"""

@app.get("/test/{name}")
def test_name_endpoint(name: str):  
    return {"msg": f"saved user {name}"}



"""
    Caesar cipher endpoint:
    POST /caesar
    Body:{ "text": string, "offset": int, "mode": "encrypt"/”decrypt”  }
    Response: { "encrypted_text": "..." } או: { "decrypted_text": "..." }

"""



@app.post("/caesar/")
def caesar_cipher(): 
    
    return {"message": "Caesar cipher endpoint not yet implemented."}


"""Fence cipher endpoints:
GET /fence/encrypt?text=<טקסט>
 Response:
{ "encrypted_text": "..." }
 """
 
@app.get("/fence/encrypt")
def fence_encrypt():  
    return {"message": "Fence cipher encrypt endpoint not yet implemented."}



"""
POST /fence/decrypt
Body: { "text": "string" }
Response: { "decrypted": "..." }
"""

@app.post("/fence/decrypt")
def fence_decrypt():  
    return {"message": "Fence cipher decrypt endpoint not yet implemented."}