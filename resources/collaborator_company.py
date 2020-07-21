from flask_restful import Resource, reqparse
from models.collaborator_company import CollaboratorCompanyModel

class CollaboratorCompany(Resource):
    parser = reqparse.RequestParser()

    def get(self, company_id):
        collaborators = CollaboratorCompanyModel.collaborators_from_company(company_id)
        return collaborators
    def put (self, company_id, collaborator_id):
        collaborator_model = CollaboratorCompanyModel(company_id, collaborator_id)
        result = collaborator_model.register_collaborator_in_company()
        return result
    def delete(self, company_id, collaborator_id):
        result = CollaboratorCompanyModel.remove_collaborator_from_company(collaborator_id)
        return result