from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):

    parser = reqparse.RequestParser()  # Just to get required key values (so that they cannot change name)
    parser.add_argument('price', type=float, required=True, help="This field cannot be left blank")
    parser.add_argument('store_id', type=int, required=True, help="This field cannot be left blank")

    @jwt_required()
    def get(self, name):
        row = ItemModel.find_by_name(name)
        if row:
            return row.json()
        else:
            return {'message': 'Item Not Found'}, 404
        return item

    def post(self, name):

        data = Item.parser.parse_args()
        if ItemModel.find_by_name(name):
            return {'message': 'A item with this name already exists'}, 400

        item = ItemModel(name, data['price'], data['store_id'])
        try:
            #item.insert()
            item.save_to_db()
        except:
            return {'message': 'An error occurred inserting the item'}, 500 # Internal Server Error

        return item.json(), 201

    @jwt_required()
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if not item:
            return {'message': 'No items exists with this name'}, 404
        try:
            item.delete()
        except:
            return {'message': 'An error occured deleting the item'}, 500

        return {'message': 'Item Deleted'}, 200

    @jwt_required()
    def put(self, name):

        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item:
            try:
                #item = ItemModel(name, data['price'])
                #item.update()
                item.price = data['price']
                item.store_id = data['store_id']
                item.save_to_db()
            except:
                return {'message': 'An error occurred updating the item'}, 500
        else:
            try:
                item = ItemModel(name, data['price'], data['store_id'])
                #item.insert()
                item.save_to_db()
            except:
                return {'message': 'An error occurred inserting the item'}, 500

            return item.json(), 201

        return item.json(), 200


class ItemList(Resource):
    @jwt_required()
    def get(self):
        #connection = sqlite3.connect("data.db")
        #cursor = connection.cursor()
        #result = cursor.execute("SELECT * from Items")
        #items = []
        #for row in result:
        #    items.append({'name': row[1], 'price': row[2]})

        #connection.close()
        #return {'items': items}, 200
        return {'items': [item.json() for item in ItemModel.query.all()]}