from db import db_connect

class CompanyModel():
    def __init__(self, name):
        self.name = name


    def insert(self):
        conn = db_connect.connect()
        conn.execute("INSERT INTO companies (name) VALUES ('%s')" % self.name)
        return {'message': 'company has been created successfully.'}, 201


    @staticmethod
    def all():
        conn = db_connect.connect()
        query = conn.execute("SELECT * FROM companies")
        return {'companies': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}

    @staticmethod
    def get_company(id):
        conn = db_connect.connect()
        query = conn.execute("SELECT * FROM companies WHERE id = %d" % int(id))
        return {'company': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
