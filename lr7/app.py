from flask import Flask, render_template  
from flask_socketio import SocketIO, emit
import requests  
import time  
import threading  

app = Flask(__name__)  
socketio = SocketIO(app)  

# Хранение состояния курсов валют  
currency_data = {}  
observers = []  

# Функция для получения курсов валют  
def fetch_currency_rates():  
    global currency_data  
    while True:  
        response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")  
        currency_data = response.json()["Valute"]  
        notify_observers()  
        time.sleep(60)  # Обновление каждую минуту  


# Уведомление наблюдателей о новых данных  
def notify_observers():  
    if observers:  
        socketio.emit('currency_update', currency_data)  

@app.route('/')  
def index():  
    return render_template('index.html')  

@socketio.on('connect')  
def handle_connect():  
    observer_id = str(len(observers) + 1)  
    observers.append(observer_id)  
    emit('client_id', observer_id)  # Отправка идентификатора клиента  

@socketio.on('disconnect')  
def handle_disconnect():  
    global observers  
    observers = [observer for observer in observers if observer != req.sid]  

if __name__ == '__main__':  
    # Запуск потока для получения курсов валют  
    thread = threading.Thread(target=fetch_currency_rates)  
    thread.start()  

    socketio.run(app)