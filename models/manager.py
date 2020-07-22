from db import db_connect
from flask_jsonpify import jsonify

class ManagerModel():

    def __init__(self, manager_id, collaborator_id):
        self.manager_id = manager_id
        self.collaborator_id = collaborator_id

        
    def allocate(self):
        conn = db_connect.connect()

        query = conn.execute("SELECT * FROM collaborators WHERE id in (%d, %d)" % (int(self.manager_id), int(self.collaborator_id)))
        collaborators = query.fetchall()
        print(collaborators)
        if (len(collaborators) != 2 or collaborators[0][3] != collaborators[1][3]):
            return {'message': 'forbidden operation.'}, 409

        query = conn.execute("SELECT * FROM managers WHERE manager_id = %d AND collaborator_id = %d" % (int(self.collaborator_id), int(self.manager_id)))
        relation = query.first()
        if (relation != None):
            return {'message': 'loop detected.'}, 409

        query = conn.execute("SELECT * FROM managers WHERE collaborator_id = %d" % int(self.collaborator_id))
        relation = query.first()
        if (relation != None):
            return {'message': 'collaborator already has manager.'}, 409

        conn.execute("INSERT INTO managers (manager_id, collaborator_id) VALUES (%d, %d)" % (int(self.manager_id), int(self.collaborator_id)))
        return {'message': 'relation has been set.'}

    @staticmethod
    def collaborators_from_manager(manager_id):
        conn = db_connect.connect()
        query = conn.execute("""SELECT cl.id, cl.name, cl.email AS company_name 
                                FROM managers AS mn 
                                INNER JOIN collaborators AS cl ON cl.id = mn.collaborator_id 
                                WHERE mn.manager_id = %d""" % int(manager_id))
        return {'collaborators': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}

    @staticmethod
    def second_level_collaborators(manager_id):
        second_level_collaborators = ManagerModel.collaborators_from_manager(manager_id)
        print(second_level_collaborators)
        print(second_level_collaborators['collaborators'])
        for collaborator in second_level_collaborators['collaborators']:
            print(collaborator)
            collaborators = ManagerModel.collaborators_from_manager(collaborator['id'])
            collaborator['collaborators'] = collaborators['collaborators']
        return second_level_collaborators
    
    @staticmethod
    def team(collaborator_id):
        manager_id = ManagerModel.manager_of(collaborator_id)
        team = ManagerModel.collaborators_from_manager(manager_id)
        return team

    @staticmethod
    def manager_of(collaborator_id):
        conn = db_connect.connect()
        query = conn.execute("SELECT * FROM managers WHERE collaborator_id = %d" % int(collaborator_id))
        relation = query.first()
        if (relation != None):
            return relation[1]
        return 0