class UsuarioRepository: 
    def __init__(self, database):
        self.db = database

    def buscar_usuarios(self):
        self.db.connect()
        self.db.execute('SELECT * FROM usuario')
        return self.db.fetchall()
    
    def buscar_usuario_id(self, id):
        self.db.connect()
        self.db.execute('''
            SELECT * FROM usuario WHERE id =?
        ''', (id,))
        return self.db.fetchone()
        
    def buscar_usuario_email(self, email):
        self.db.connect()
        self.db.execute('''
            SELECT * FROM usuario WHERE email =?
        ''', (email,))
        return self.db.fetchall()
    
    def inserir_usuario(self, nome, apelido, email):
        self.db.connect()
        self.db.execute('''
            INSERT INTO usuario(nome, apelido, email, data_cadastro) 
            VALUES (?, ?, ?, DATETIME('now', 'localtime'))
        ''', (nome, apelido, email))
        usuario_novo_id = self.db.lastrowid()
        self.db.commit()
        return self.buscar_usuario_id(usuario_novo_id)
    