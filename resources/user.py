import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('username',
        type=str,
        required=False,
        help="This username should be given in string and should not be empty"
    )

    parser.add_argument('password',
        type=str,
        required=True,
        help="This password should be given in string and should not be empty"
    )


    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']) is not None:
            return {"message":"The user with this name is already present. Please change the username and try."},400
        user = UserModel(data['username'],data['password'])
        # user = UserModel(**data)
        user.save_to_db()
        return {"message":"User created successfully"}, 201
