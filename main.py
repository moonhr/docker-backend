# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import logging

app = FastAPI()

origins = [
    "http://localhost:3000",
]

# CORS 미들웨어 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # 허용할 출처 목록
    allow_credentials=True,           # 쿠키 등 자격 증명 허용 여부
    allow_methods=["*"],              # 허용할 HTTP 메서드
    allow_headers=["*"],              # 허용할 HTTP 헤더
)

# 로깅 설정
logging.basicConfig(level=logging.INFO)

class Item(BaseModel):
    name: str

@app.post("/items/")
async def create_item(item: Item):
    logging.info(f"Received item: {item.name}")
    return {"message": f"Item '{item.name}' received"}

@app.get("/data")
async def get_data():
    sample_data = {"message": "Hello from FastAPI!"}
    return sample_data