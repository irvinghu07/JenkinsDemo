from flask import Flask
from fibo import Fibo
import sys

app = Flask(__name__)
PORT = 7777


@app.route('/hello')
def hello_world():
    return 'Hello Jenkins'


@app.route('/fibo/<b>')
def get_fibo(b: str):
    if b.isnumeric():
        fibo = Fibo(int(b, 10))
        out = fibo.cal_fibo()
        return f"The {fibo.boarder + 1}th elements in fibonacci is :{out}"
    return "Invalid input"


def main():
    if len(sys.argv) == 2:
        p = sys.argv[1]
    else:
        p = PORT
    app.run(port=p)


if __name__ == '__main__':
    main()
