from flask_restful import Resource, reqparse
from models.manager import ManagerModel

class Manager(Resource):
    def post(self, manager_id, collaborator_id):
        manager_model = ManagerModel(manager_id, collaborator_id)
        result = manager_model.allocate()
        return result
    
    def get(self, manager_id):
        result = ManagerModel.collaborators_from_manager(manager_id)
        return result

class Managers(Resource):
    def get(self, manager_id):
        result = ManagerModel.second_level_collaborators(manager_id)
        return result
        
class Team(Resource):
    def get(self, collaborator_id):
        result = ManagerModel.team(collaborator_id)
        return result