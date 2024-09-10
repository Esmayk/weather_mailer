class Usuario: 
    def __init__(self, id, nome, apelido, email, data_cadastro):
        self.id = id
        self.nome = nome
        self.apelido = apelido
        self.email = email
        self.data_cadastro = data_cadastro

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'apelido': self.apelido,
            'email': self.email,
            'data_cadastro': self.data_cadastro
        }