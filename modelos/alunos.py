from modelos.avaliaçao import Avaliacao

class Alunos:
    alunos = []

    def __init__(self, nome, idade, objetivo, local):
        self._nome = nome.upper()
        self._idade = idade
        self._objetivo = objetivo.title()
        self._local = local.title()
        self._matriculado = True
        self._valor_mensalidade = []
        Alunos.alunos.append(self)

    def __str__(self):
        return f'{self._nome} | {self._idade} | {self._objetivo} | {self._local} | {self.matriculado}'

    @classmethod
    def listar_alunos(cls):
        print('''            ▄▀█ █░░ █░█ █▄░█ █▀█ █▀   █▀▄ ▄▀█   █▀█ █▀▀ █ █▀   █▀▀ █▄█ █▀▄▀█
                             █▀█ █▄▄ █▄█ █░▀█ █▄█ ▄█   █▄▀ █▀█   █▀▄ ██▄ █ ▄█   █▄█ ░█░ █░▀░█ ''')

        print(f'{"Nome do Aluno".ljust(20)} | {"Idade".ljust(6)} | {"Objetivo".ljust(20)} | {"Local".ljust(20)} | {"Matrícula".ljust(20)} | {"Média Mensalidade"}')
        print('------------------------------------------------------------------------------------------------------------------------------')
        for aluno in cls.alunos:
            print(f'{aluno._nome.ljust(20)} | {str(aluno._idade).ljust(6)} | {aluno._objetivo.ljust(20)} | {aluno._local.ljust(20)} | {aluno.matriculado.ljust(20)} | {aluno.media_mensalidade}')
            print('-------------------------------------------------------------------------------------------------------------------------')

    @property
    def matriculado(self):
        return '✅ Matriculado' if self._matriculado else '❌ Não Matriculado'

    def alterar_estado(self):
        self._matriculado = not self._matriculado

    def receber_preço(self, academia, preço):
        preço = Avaliacao(academia, preço)
        self._valor_mensalidade.append(preço)

    @property
    def media_mensalidade(self):
        if not self._valor_mensalidade:
            return 0
        somas_das_mensalidades = sum(valor._preço for valor in self._valor_mensalidade)
        quantidade_academias = len(self._valor_mensalidade)
        media = round(somas_das_mensalidades / quantidade_academias, 1)
        return media

aluno_joao = Alunos('Reis', 21, 'Hipertrofia', 'Academia A')
aluno_maria = Alunos('Bia', 20, 'Emagrecimento', 'Academia A')
aluno_pedro = Alunos('Vaida', 50, 'Resistência', 'Academia C')

Alunos.listar_alunos()
     