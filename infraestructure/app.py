import json

from attr import asdict
from flask import Flask, jsonify, request

from application.use_cases import UserCreator, UserRetriever
from infraestructure.ram_repo import RamRepository

app = Flask(__name__)

ram_repository = RamRepository()
creator = UserCreator(ram_repository)
creator.create_user(user_name='user_1', password='abc', name='Juan')
creator.create_user(user_name='user_2', password='abc', name='Paco')
creator.create_user(user_name='user_3', password='abc', name='Pedro')


@app.route('/users/<int:user_id>/')
def get_users(user_id):
    user_retriever = UserRetriever(ram_repository)
    user = user_retriever.get_user_by_id(user_id)
    return jsonify(asdict(user))


@app.route('/users/', methods=['POST'])
def create_users():
    body = json.loads(request.data)
    user = creator.create_user(user_name=body.get('user_name'), password=body.get('password'), name=body.get('name'))
    return jsonify(asdict(user))


app.run()
