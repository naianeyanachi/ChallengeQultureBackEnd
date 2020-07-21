from flask import Flask, request
from flask_restful import Resource, Api
from db import db_connect
from json import dumps
from flask_jsonpify import jsonify

from resources.company import Company, Companies
from resources.collaborator import Collaborator, Collaborators
from resources.collaborator_company import CollaboratorCompany

app = Flask(__name__)
api = Api(app)


api.add_resource(Companies, '/companies')
api.add_resource(Company, '/company/<id>', '/company')

api.add_resource(Collaborators, '/collaborators')
api.add_resource(Collaborator, '/collaborator/<id>', '/collaborator')

api.add_resource(CollaboratorCompany, '/company/<company_id>/collaborator/<collaborator_id>', '/company/<company_id>/collaborators')


if __name__ == '__main__':
    app.run()