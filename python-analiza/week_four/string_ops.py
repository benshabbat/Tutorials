from fastapi import FastAPI
from pydantic import BaseModel
import json
import os


app = FastAPI()

@app.get("/fraturs/reverse")
async def reverse_string(s: str):
    return {"original": s, "reversed_text": s[::-1]}

@app.get("/fraturs/uppercase/{text}")
async def uppercase_string(text: str):
    return {"original": text, "uppercased": text.upper()}

@app.post("/fraturs/remove-vowels")
async def remove_vowels(text: str):
    vowels = "aeiouAEIOU"
    without_vowels = ""
    for char in text:
        if char not in vowels:
            without_vowels += char
    # without_vowels = ''.join([char for char in text if char not in vowels])
    return {"original": text, "without_vowels": without_vowels}

@app.post("/fraturs/remove-every-third")
async def remove_every_third(text: str):
    modified_text = ""
    for index, char in enumerate(text):
        if (index + 1) % 3 != 0:
            modified_text += char
    # modified_text = ''.join([char for index, char in enumerate(text) if (index + 1) % 3 != 0])
    return {"original": text, "result": modified_text}


@app.get("/fraturs/letter-counts")
async def letter_counts(text: str):
    text_letter_counts = {}
    set_text = set(text)
    for letter in set_text:
        text_letter_counts[letter] = text.count(letter)
        
    object_to_save = {
        "original": text,
        "counts": text_letter_counts,   
    }
    
    # Create data directory if it doesn't exist
 
    os.makedirs("data", exist_ok=True)
  
    with open("data/letter_counts.json", "w") as f:
        json.dump(object_to_save, f) 
          
    return {
        "original": text,
        "counts": text_letter_counts,   
        "saved_to": "data/letter_counts.json"
    }
  
