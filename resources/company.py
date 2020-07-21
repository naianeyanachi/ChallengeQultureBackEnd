from flask_restful import Resource, reqparse
from models.company import CompanyModel
from db import db_connect

class Company(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str)

    def get(self, id):
        company = CompanyModel.get_company(id)
        return company
    def post(self):
        data = Company.parser.parse_args()
        company_model = CompanyModel(data['name'])
        result = company_model.insert()
        return result

class Companies(Resource):
    def get(self):
        all_companies = CompanyModel.all()
        return all_companies