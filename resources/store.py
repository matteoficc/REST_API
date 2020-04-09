from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):

    @staticmethod
    def get(name):
        store = StoreModel.find_by_name(name=name)
        if store:
            return store.json()
        return {'message': 'Store not found'}, 404

    @staticmethod
    def post(name):
        if StoreModel.find_by_name(name=name):
            return {'message': f'A store with name {name} already exists'}, 400

        store = StoreModel(name=name)
        try:
            store.save_to_db()
        except:
            return {'message': 'An error occurred while creating the store'}, 500

        return store.json(), 201

    @staticmethod
    def delete(name):
        store = StoreModel.find_by_name(name=name)
        if store:
            store.delete()

        return {'message': 'Store deleted'}


class StoreList(Resource):
    @staticmethod
    def get():
        return {'store': [store.json() for store in StoreModel.query.all()]}
