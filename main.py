from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def roblox_communication():
    # Защита: пробуем прочитать как форму (UrlEncoded), если не вышло — как JSON
    if request.form:
        input_value = request.form.get("value", "")
    elif request.is_json:
        data = request.get_json() or {}
        input_value = data.get("value", "")
    else:
        # Если пришло что-то совсем непонятное, берем сырой текст
        input_value = request.data.decode('utf-8', errors='ignore')

    # Наша логика: перевод в заглавные буквы
    output_value = str(input_value).upper()
    
    # Возвращаем ответ обратно в Roblox
    return jsonify({"value": output_value})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
