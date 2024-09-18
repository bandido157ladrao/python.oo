class Alunos:
    alunos = []

    def __init__(self, nome, idade, objetivo, local):
        self.nome = nome
        self.idade = idade
        self.objetivo = objetivo
        self.local = local
        self._matriculado = True
        Alunos.alunos.append(self)

    def __str__(self):
        return f'{self.nome} | {self.idade} | {self.objetivo} | {self.local} | {self.matriculado}'

    @staticmethod
    def listar_alunos():
        print('')        
        print('''
                             ▄▀█ █░░ █░█ █▄░█ █▀█ █▀   █▀▄ ▄▀█   █▀█ █▀▀ █ █▀   █▀▀ █▄█ █▀▄▀█
                             █▀█ █▄▄ █▄█ █░▀█ █▄█ ▄█   █▄▀ █▀█   █▀▄ ██▄ █ ▄█   █▄█ ░█░ █░▀░█''')
        
        print(f'{"Nome do Aluno".ljust(20)} | {"Idade".ljust(6)} | {"Objetivo".ljust(20)} | {"Local".ljust(20)} | {"Matrícula"}')
        print('------------------------------------------------------------------------------------------------------------------------------')
        for aluno in Alunos.alunos:
            print(f'{aluno.nome.ljust(20)} | {str(aluno.idade).ljust(6)} | {aluno.objetivo.ljust(20)} | {aluno.local.ljust(20)} | {aluno.matriculado}')
            print('-------------------------------------------------------------------------------------------------------------------------')

    @property
    def matriculado(self):
        return '✅ Matriculado' if self._matriculado else '❌ Não Matriculado'        

aluno_joao = Alunos('Reis', 25, 'Hipertrofia', 'Academia A')
aluno_maria = Alunos('Vaida', 50, 'Emagrecimento', 'Academia B')
aluno_pedro = Alunos('Bia', 22, 'Resistência', 'Academia A')

Alunos.listar_alunos()

