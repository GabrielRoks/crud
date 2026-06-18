from cls.alunos import Aluno
from cls.turma import Turma

def menu():

    turma = Turma()

    while True:

        print("\n===== DIÁRIO DE CLASSE =====")
        print("1 - Matricular novo aluno")
        print("2 - Lançar nota")
        print("3 - Exibir boletim")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":

            matricula = int(input("Matrícula: "))
            nome = input("Nome: ")

            aluno = Aluno(matricula, nome)

            turma.matricular_aluno(aluno)

        elif opcao == "2":

            matricula = int(input("Matrícula do aluno: "))
            nota = float(input("Nota: "))

            turma.atribuir_nota(matricula, nota)

        elif opcao == "3":

            turma.boletim()

        elif opcao == "4":

            print("Encerrando o sistema...")
            break

        else:

            print("Opção inválida.")


menu()