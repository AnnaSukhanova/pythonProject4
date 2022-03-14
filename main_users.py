import sqlite3

from flask import Flask
from data.db_session import global_init, create_session
from data.users import User

sqlite3.connect('./db/blogs.db')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    global_init(input())

    session = create_session()

    for user in session.query(User).filter(User.address == "module_1", User.age < 21):
        user.address = "module_3"
    session.commit()

    app.run(host='127.0.0.1', port=5000)


if __name__ == '__main__':
    main()
