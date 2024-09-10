import sqlite3

class Database:
    def __init__(self):
        self.nome_banco = 'app/db/weathermailer.db'
        self.conexao = None
        self.cursor = None

    def connect(self):
        self.conexao = sqlite3.connect(self.nome_banco)
        self.cursor = self.conexao.cursor()
    
    def close(self):
        if self.conexao:
            self.conexao.close()
    
    def execute(self, query, params=()):
        self.cursor.execute(query, params)

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()
    
    def rollback(self):
        if self.conexao:
            self.conexao.rollback()

    def commit(self):
        if self.conexao:
            self.conexao.commit()

    def lastrowid(self):
        if self.conexao:
            return self.cursor.lastrowid