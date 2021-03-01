from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from flask import Flask, request, render_template
import codecs
app = Flask(__name__)

engine = create_engine('sqlite:///user.db')  # データベース名を宣言
Base = declarative_base()  # データベースのテーブルの親


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, unique=True)
    email = Column(String)
    name = Column(String)

    def __repr__(self):
        return "User<{}, {}, {}>".format(self.id, self.email, self.name)


Base.metadata.create_all(engine)  # データベースを構築
SessionMaker = sessionmaker(bind=engine)  # Pythonとデータベースの経路
session = SessionMaker()  # 経路を作成

# Userインスタンス作成
user1 = User(email="thisisme@test.com", name="Python")
session.add(user1)  # user1 をデータベースに入力するための準備
session.commit()  # データベースにデータを入れる


@app.route("/db")
def menu():
  user = session.query(User).get(1)
  return render_template("a.html", user = user)