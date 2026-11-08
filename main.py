from fastapi import FastAPI, Header, Form, Query, HTTPException
from typing import Optional
import uvicorn

app = FastAPI(title="Передатчик HTTP Сервер")

# Настраиваем тот же самый путь (эндпоинт), что и у другого чела: /typewriter/read
# Делаем поддержку как POST, так и GET запросов

@app.post("/typewriter/read")
async def typewriter_post(
    value: str = Form(default="00000000"),
    sid: Optional[str] = Header(None)  # Читаем заголовок 'sid' из игры
):
    print(f"\n[POST /typewriter/read] Запрос от игры!")
    print(f"-> Заголовок sid: {sid}")
    print(f"-> Параметр value: {value}")
    
    # Сюда можно добавить код, который будет выполняться при получении данных
    
    # Ответ, который возвращается в игру
    return {
        "status": "success",
        "msg": "Данные успешно прочитаны сервером",
        "your_sid": sid
    }

@app.get("/typewriter/read")
async def typewriter_get(
    value: str = Query(default="00000000"),
    sid: Optional[str] = Header(None)
):
    print(f"\n[GET /typewriter/read] Запрос от игры!")
    print(f"-> Заголовок sid: {sid}")
    print(f"-> Параметр value: {value}")
    
    return {
        "status": "success",
        "msg": "Сервер готов к работе",
        "your_sid": sid
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=50200, reload=True)
