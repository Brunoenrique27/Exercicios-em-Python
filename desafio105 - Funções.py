def notas(*n , sit = False):
    """-> Função para analisar notas e situaçoes dos alunos.
    :param n: notas dos alunos.
    :param aluno: um dicionario com as informações.
    :param sit: o usuario define se quer ver ou nao a situação do aluno.
    :param return aluno: imprime os valores na tela com as informaçoes do aluno."""
    aluno = {}
    aluno['total'] = len(n)
    aluno['maior'] = max(n)
    aluno['menor'] = min(n)
    aluno['media'] = sum(n) / len(n)
    if sit:
        if aluno['media'] >= 7:
            aluno['situaçao'] = 'BOA'
        elif aluno['media'] >= 5:
            aluno['situaçao'] = 'RAZOAVEL'
        else:
            aluno['situaçao'] = 'RUIM'
    return aluno

resp = notas(5.5, 9.5, 10, 6.5, sit =True)
print(resp)
