from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Создаем модель для валидации входящего JSON от мода
class TransmitterData(BaseModel):
    value: str

@app.post("/")
async def handle_post_request(data: TransmitterData):
    print(f"\n[Входящий POST] Получен JSON:")
    print(f"-> value = {data.value}")
    return {"status": "success", "echo_value": data.value}

@app.get("/")
async def handle_get_request():
    return {"status": "running"}

if __name__ == "__main__":
    # Запускаем локально на порту 50200
    uvicorn.run("main:app", host="127.0.0.1", port=50200, reload=True)
