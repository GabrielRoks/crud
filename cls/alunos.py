class Aluno:
    def __init__(self, matricula, nome):
        self.matricula = matricula
        self.nome = nome
        self.notas = []

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0

        return sum(self.notas) / len(self.notas)


