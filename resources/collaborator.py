from flask_restful import Resource, reqparse
from models.collaborator import CollaboratorModel
from db import db_connect

class Collaborator(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str)
    parser.add_argument('email', type=str)
    parser.add_argument('company_id', type=str)

    def get(self, id):
        collaborator = CollaboratorModel.get_collaborator(id)
        return collaborator
    def post(self):
        data = Collaborator.parser.parse_args()
        collaborator_model = CollaboratorModel(data['name'], data['email'], data['company_id'])
        result = collaborator_model.insert()
        return result
    def delete(self, id):
        result = CollaboratorModel.delete_collaborator(id)
        return result


class Collaborators(Resource):
    def get(self):
        all_collaborators = CollaboratorModel.all()
        return all_collaborators