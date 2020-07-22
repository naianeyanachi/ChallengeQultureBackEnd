from flask import Flask, request
from flask_restful import Resource, Api
from db import db_connect
from json import dumps
from flask_jsonpify import jsonify

from resources.company import Company, Companies
from resources.collaborator import Collaborator, Collaborators
from resources.collaborator_company import CollaboratorCompany
from resources.manager import Manager, Managers, Team

app = Flask(__name__)
api = Api(app)


api.add_resource(Companies, '/companies')
api.add_resource(Company, '/company/<id>', '/company')

api.add_resource(Collaborators, '/collaborators')
api.add_resource(Collaborator, '/collaborator/<id>', '/collaborator')

api.add_resource(CollaboratorCompany, '/company/<company_id>/collaborator/<collaborator_id>', '/company/<company_id>/collaborators')

api.add_resource(Manager, "/manager/<manager_id>/collaborators", "/manager/<manager_id>/collaborator/<collaborator_id>")
api.add_resource(Managers, "/manager/<manager_id>/managers/collaborators")
api.add_resource(Team, "/collaborator/<collaborator_id>/team")

if __name__ == '__main__':
    app.run()