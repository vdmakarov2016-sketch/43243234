frfrom fastapi import FastAPI, Form, Query, Request
import uvicorn

# Создаем приложение FastAPI
app = FastAPI(title="HTTP Transmitter Receiver")

# 1. Обработка POST-запросов (так как в интерфейсе указан тип Content-Type: ApplicationUrlEncoded)
@app.post("/")
async def handle_post_request(value: str = Form(default="00000000")):
    """
    Принимает POST-запрос от передатчика.
    Автоматически парсит 'value' из формата ApplicationUrlEncoded.
    """
    print(f"\n[Входящий POST] Получены данные:")
    print(f"-> value = {value}")
    
    # Здесь вы можете добавить свою логику (например, запись в файл или управление игрой)
    
    return {
        "status": "success",
        "message": "Data received via POST",
        "echo_value": value
    }

# 2. Обработка GET-запросов (на случай, если передатчик отправляет данные через URL-параметры)
@app.get("/")
async def handle_get_request(value: str = Query(default="00000000")):
    """
    Принимает GET-запрос от передатчика (например: http://127.0.0)
    """
    print(f"\n[Входящий GET] Получены данные:")
    print(f"-> value = {value}")
    
    return {
        "status": "success",
        "message": "Data received via GET",
        "echo_value": value
    }

# Точка входа для запуска сервера в Windows
if __name__ == "__main__":
    print("Запуск Python-сервера для Передатчика HTTP...")
    uvicorn.run(
        "main:app", 
        host="0.0.0.0",  # Открывает сервер для локальной сети (чтобы передатчик мог достучаться)
        port=50200,      # Порт, который вы выбрали (можно заменить на 5000)
        reload=True      # Сервер будет сам перезагружаться при изменении этого файла
    )
