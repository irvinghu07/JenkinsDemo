from flask import Flask
from flask import request
from fibo import Fibo
import socket

app = Flask(__name__)


def hostname():
    return socket.gethostbyname(socket.gethostname())


@app.route('/hello')
def hello_world():
    return f'Hello Jenkins at === {hostname()}/{request.remote_addr}'


@app.route('/fibo/<b>')
def get_fibo(b: str):
    if b.isnumeric():
        fibo = Fibo(int(b, 10))
        out = fibo.cal_fibo()
        return f"The {fibo.boarder}th elements in fibonacci is :{out} === {hostname()}/{request.remote_addr}"
    return f"Invalid input at ip:{hostname()}"


if __name__ == '__main__':
    app.run(host="0.0.0.0")
