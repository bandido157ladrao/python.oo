class Aluno:
    alunos=[]

    def __init__(self, nome, idade, turno):
        self.nome = nome
        self.idade = idade
        self.turno = turno
        self.matricula = False
        Aluno.alunos.append(self)

    def __str__(self):
        return {f'{self.nome} | {self.idade} | {self.turno}'}
                                               
    def listar_alunos():                                       
        for alunos in Aluno.alunos:                                       
        print(f'{cliente.nome} | {cliente.idade} | {cliente.turno}')                                      
                                              
aluno_Reis = Aluno('Eduardo', '17', 'Manha')
aluno_Bia = Aluno('Bia', '17', 'Tarde')

aluno_Reis.nome = 'Reis'
aluno_Bia.nome = 'Bia'

alunos = [aluno_Reis, aluno_Bia]

