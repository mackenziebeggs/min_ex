import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()                    
                       
origins = [   
    "http://localhost:5173",
    "https://localhost:5173",
]            
                                                         
app.add_middleware(
    CORSMiddleware,            
    allow_origins=origins,  
    allow_credentials=True,    
    allow_methods=["*"],
    allow_headers=["*"],
)                                                                                                                        
                                               
@app.post("/endpoint")
async def endpoint():
    return {"message": "Hello, world!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
