import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.store import StoreModel


class Store(Resource):

    @jwt_required()
    def get(self, name):
        row = StoreModel.find_by_name(name)
        if row:
            return row.json()
        else:
            return {'message': 'Store Not Found'}, 404
        return item

    def post(self, name):

        if StoreModel.find_by_name(name):
            return {'message': 'A store with this name already exists'}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': 'An error occurred inserting the item'}, 500  # Internal Server Error

        return store.json(), 201

    @jwt_required()
    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if not store:
            return {'message': 'No stores exists with this name'}, 404
        try:
            store.delete()
        except:
            return {'message': 'An error occured deleting the store'}, 500

        return {'message': 'Store Deleted'}, 200


class StoreList(Resource):
    @jwt_required()
    def get(self):
        return {'stores': [item.json() for item in StoreModel.query.all()]}