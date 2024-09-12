class Aluno:
    def __init__(self, nome, idade, turno):
        self.nome = nome
        self.idade = idade
        self.turno = turno
        self.matricula = False

aluno_Reis = Aluno('Eduardo', '17', 'Manha')
aluno_Bia = Aluno('Bia', '17', 'Tarde')

aluno_Reis.nome = 'Reis'
aluno_Bia.nome = 'Bia'

alunos = [aluno_Reis, aluno_Bia]

