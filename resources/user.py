from flask_restful import Resource, reqparse
from models.user import UserModel


# Resource is an external representation of an entity
class UserRegister(Resource):
    parser = reqparse.RequestParser()  # Just to get required key values (so that they cannot change name)
    parser.add_argument('username', type=str, required=True, help="This field cannot be left blank")
    parser.add_argument('password', type=str, required=True, help="This field cannot be left blank")

    def post(self):

        data = UserRegister.parser.parse_args()

        if UserModel.find_by_id(data['username']):
            return {'message': 'A user with this username already exists'}, 400

        #connection = sqlite3.connect("data.db")
        #cursor = connection.cursor()
        #cursor.execute("INSERT INTO Users values (NULL, ?, ?) ", (data['username'], data['password']))
        #connection.commit()
        #connection.close()
        user = UserModel(**data)
        user.save_to_db()
        return {'message': 'User created successfully'}, 200

