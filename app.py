from modelos.alunos import Alunos

aluno_joao = Alunos('João', 25, 'Hipertrofia', 'Academia A')
aluno_maria = Alunos('Maria', 30, 'Emagrecimento', 'Academia B')
aluno_pedro = Alunos('Pedro', 22, 'Resistência', 'Academia C')

aluno_joao.alterar_estado()
aluno_pedro.receber_preço('Academia A', 150)
aluno_pedro.receber_preço('Academia B', 120)
aluno_pedro.receber_preço('Academia C', 130)

def main():
    Alunos.listar_alunos()

if __name__ == '__main__':
    main()




