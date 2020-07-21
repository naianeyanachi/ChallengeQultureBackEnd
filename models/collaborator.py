from db import db_connect

class CollaboratorModel():

    def __init__(self, name, email, company_id):
        self.name = name
        self.email = email
        self.company_id = company_id


    def insert(self):
        conn = db_connect.connect()
        conn.execute("INSERT INTO collaborators (name, email, company_id) VALUES ('%s', '%s', %d)" % (self.name, self.email, int(self.company_id)))
        return {'message': 'collaborator has been created successfully.'}, 201


    @staticmethod
    def all():
        conn = db_connect.connect()
        query = conn.execute("SELECT * FROM collaborators")
        return {'collaborators': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}

    @staticmethod
    def get_collaborator(id):
        conn = db_connect.connect()
        query = conn.execute("""SELECT cl.id, cl.name, cl.email, cl.company_id, cp.name AS company_name 
                                FROM collaborators AS cl 
                                INNER JOIN companies AS cp ON cl.company_id = cp.id 
                                WHERE cl.id = %d""" % int(id))
        return {'collaborator': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}

    @staticmethod
    def delete_collaborator(id):
        conn = db_connect.connect()
        conn.execute("DELETE FROM collaborators WHERE id = %d" % int(id))
        return {'message': 'collaborator has been deleted.'}