import redis
from flask import Flask

app = Flask(__name__)


@app.route('/user/<int:identify>')
def get(identify):
    r = redis.StrictRedis(host='192.168.6.167', port=6379, db=0)
    username = r.get(identify)
    if username is None:
        return "not fount", 404
    else:
        return username


if __name__ == '__main__':
    app.run()