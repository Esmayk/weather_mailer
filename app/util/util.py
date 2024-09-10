class Util:
    def __init__(self):
        self.fator_conversao = 1.943844

    def convert_metros_nos(self, velocidade_vento):
        return round(velocidade_vento * self.fator_conversao , 2) 