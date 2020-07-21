from db import db_connect

class CollaboratorCompanyModel():

    def __init__(self, company_id, collaborator_id):
        self.company_id = company_id
        self.collaborator_id = collaborator_id

        
    def register_collaborator_in_company(self):
        conn = db_connect.connect()
        conn.execute("UPDATE collaborators SET company_id = %d WHERE id = %d" % (int(self.company_id), int(self.collaborator_id)))
        return {'message': 'collaborator has been registered.'}

    @staticmethod
    def collaborators_from_company(company_id):
        conn = db_connect.connect()
        query = conn.execute("SELECT cl.id, cl.name, cl.email FROM collaborators AS cl WHERE company_id = %d" % int(company_id))
        return {'collaborators': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}

    @staticmethod
    def remove_collaborator_from_company(collaborator_id):
        conn = db_connect.connect()
        conn.execute("UPDATE collaborators SET company_id = null WHERE id = %d" % int(collaborator_id))
        return {'message': 'collaborator has been removed.'}