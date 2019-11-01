import sqlite3
from db import db


# Model is an internal representation of an entity
class UserModel(db.Model):
    __tablename__ = "Users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        #self.id = id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):

        #connection = sqlite3.connect("data.db")
        #cursor = connection.cursor()
        #result = cursor.execute("SELECT * from Users WHERE username = ? ", (username,))
        # Value should always be a tuple - so, add comma
        #row = result.fetchone()
        #if row:
        #    user = cls(*row)  # cls(row[0], row[1], row[2])
        #else:
        #    user = None
        #connection.close()
        #return user
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, id):

        #connection = sqlite3.connect("data.db")
        #cursor = connection.cursor()
        #result = cursor.execute("SELECT * from Users WHERE id = ? ", (id,))
        # Value should always be a tuple - so, add comma
        #row = result.fetchone()
        #if row:
        #    user = cls(*row)
        #else:
        #    user = None
        #connection.close()
        #return user
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
