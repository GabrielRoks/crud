from .alunos import Aluno

class Turma:
    def __init__(self):
        self.alunos = []
    
    def calcular_media(self):
        self.alunos = []

    def matricular_aluno(self, aluno):
        for a in self.alunos:
            if a.matricula == aluno.matricula:
                print("Essa matrícula já foi adicionada anteriormente.")
                return

        self.alunos.append(aluno)
        print("Matrícula realizada com sucesso")

    def atribuir_nota(self, matricula, nota):
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                aluno.notas.append(nota)
                print("Nota atribuída")
                return
            
        print("Aluno não cadastrado")

    def boletim(self):
        if len(self.alunos) == 0:
            print("Nenhum aluno encontrado")

        for aluno in self.alunos:

            media = aluno.calcular_media()

            if media >= 7:
                status = "Aluno aprovado"
            
            else:
                status = "Aluno reprovado"
            
            print(f'Matrícula: {aluno.matricula}')
            print(f'Nome: {aluno.nome}')
            print(f'Média: {media:.2f}')
            print(f'Status: {status}')
    