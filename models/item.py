#import sqlite3
from db import db


class ItemModel(db.Model):
    __tablename__ = "Items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(90))
    price = db.Column(db.Float(precision=2))
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))

    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price, 'store_id': self.store_id}

    @classmethod
    def find_by_name(cls, name):
        #connection = sqlite3.connect("data.db")
        #cursor = connection.cursor()
        #result = cursor.execute("SELECT * from Items WHERE name = ? ", (name,))
        #row = result.fetchone()
        #connection.close()
        #if row:
        #    return cls(*row)
        #else:
        #    return None

        return cls.query.filter_by(name=name).first()  # SELECT * from Items WHERE name = name LIMIT 1

    #def insert(self)
    def save_to_db(self):
        #connection = sqlite3.connect("data.db")
        #cursor = connection.cursor()
        #cursor.execute("INSERT INTO Items VALUES (?,?) ", (self.name, self.price))
        #connection.commit()
        #connection.close()
        db.session.add(self)
        db.session.commit()

    def delete(self):
        #connection = sqlite3.connect("data.db")
        #cursor = connection.cursor()
        #cursor.execute("DELETE from Items WHERE name = ? ", (self.name, ))
        #connection.commit()
        #connection.close()
        db.session.delete(self)
        db.session.commit()

    #def update(self):
    #    connection = sqlite3.connect("data.db")
    #    cursor = connection.cursor()
    #    cursor.execute("Update Items SET price = ? WHERE name = ? ", (self.price, self.name))
    #    connection.commit()
    #    connection.close()
