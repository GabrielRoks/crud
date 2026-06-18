# crud

Título do Projeto: Sistema de Diário de Classe (Orientado a Objetos)
Cenário:
Você foi encarregado de criar um sistema simples de "Diário de Classe" para professores. O objetivo é cadastrar alunos e registrar suas notas, utilizando Orientação a Objetos e Listas.

1. Modelagem das Classes:
   Crie as seguintes classes:
   Classe Aluno: Representa o estudante. O construtor deve inicializar os atributos Matrícula (Inteiro), Nome (Texto) e Notas (uma Lista inicialmente vazia). Deve conter também um método calcular_media() que soma as notas da lista e retorna a média aritmética.
   Classe Turma: Representa o gerenciador da sala. O construtor deve inicializar uma Lista vazia para armazenar os objetos da classe Aluno.
2. Métodos da Classe Turma:
   Matricular Aluno: Recebe um objeto Aluno e o adiciona à lista da turma. Não permitir matrículas duplicadas.
   Lançar Nota: Recebe a matrícula do aluno e o valor de uma nota. Localiza o objeto Aluno correspondente e adiciona a nota à lista de notas daquele objeto.
   Exibir Boletim: Percorre a lista de alunos. Para cada objeto Aluno, imprime a Matrícula, o Nome e o resultado do método calcular_media(). Se a média for maior ou igual a 7.0, exibir "Aprovado", caso contrário, "Reprovado".
3. Menu Principal:
   Instancie um objeto da classe Turma. Utilize um laço de repetição para exibir o menu interativo:Matricular Novo AlunoLançar Nota para um AlunoExibir Boletim da TurmaSair
