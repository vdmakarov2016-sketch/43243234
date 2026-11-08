import sys
import traceback

try:
    from fastapi import FastAPI, Header, Form, Query
    from fastapi.responses import JSONResponse  # <-- Добавили специальный ответ
    from typing import Optional
    import uvicorn

    app = FastAPI(title="HTTP Transmitter Server")

    @app.post("/typewriter/read")
    async def typewriter_post(
        value: str = Form(default="00000000"),
        sid: Optional[str] = Header(None)
    ):
        print(f"\n[Входящий POST] Данные из игры:")
        print(f"-> sid = {sid}")
        print(f"-> value = {value}")
        
        # Возвращаем строгий JSON с кодом 200, который игра гарантированно прочитает
        return JSONResponse(
            status_code=200,
            content={"status": "success", "echo_value": value}
        )

    @app.get("/typewriter/read")
    async def typewriter_get(
        value: str = Query(default="00000000"),
        sid: Optional[str] = Header(None)
    ):
        print(f"\n[GET /typewriter/read] Проверка связи:")
        print(f"-> sid = {sid}")
        print(f"-> value = {value}")
        
        return JSONResponse(
            status_code=200,
            content={"status": "success", "echo_value": value}
        )

    if __name__ == "__main__":
        print("Запуск Python-сервера для игры...")
        uvicorn.run(app, host="0.0.0.0", port=50200)

except Exception as e:
    print("\n[КРИТИЧЕСКАЯ ОШИБКА ПРИ ЗАПУСКЕ С КРЕШЕМ]:")
    print(e)
    traceback.print_exc()

finally:
    print("\nКонсоль заблокирована от вылета. Нажмите Enter для закрытия...")
    input()
