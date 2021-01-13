from flask import Flask
from fibo import Fibo
import socket

app = Flask(__name__)
PORT = 7777


def ip():
    return socket.gethostbyname(socket.gethostname())


@app.route('/hello')
def hello_world():
    return f'Hello Jenkins at ip: {ip()}'


@app.route('/fibo/<b>')
def get_fibo(b: str):
    if b.isnumeric():
        fibo = Fibo(int(b, 10))
        out = fibo.cal_fibo()
        return f"The {fibo.boarder}th elements in fibonacci is :{out} at ip:{ip()}"
    return f"Invalid input at ip:{ip()}"


if __name__ == '__main__':
    app.run(host="0.0.0.0")
