quantidade_alunos = int(input("Quantos alunos? "))
aprovados = 0
reprovados = 0
media_turma = 0
maior_media = None
menor_media = None
aluno_maior_media = ""
aluno_menor_media = ""

def calcular_media(n1, n2, n3) -> float:
    media = (n1+n2+n3)/3
    return media

def situacao(media) -> str:
    if media >= 7:
        return 1, 0
    elif 5 <= media < 7:
        return 0, 0
    else:
        return 0, 1

#retirar global das funções e que cada função retorne valores
def ranking_media(media, nome_aluno, maior_media, menor_media, aluno_maior_media, aluno_menor_media):
    if maior_media is None:
        return media, media, nome, nome
    elif media > maior_media:
        aluno_maior_media = nome_aluno
        maior_media = media
    elif media < menor_media:
        aluno_menor_media= nome_aluno
        menor_media = media
    return maior_media, menor_media, aluno_maior_media, aluno_menor_media

for i in range(quantidade_alunos):
    nome = input("Nome: ")
    nota_1 = int(input("Notas: "))
    nota_2 = int(input("Notas: "))
    nota_3 = int(input("Notas: "))

    media = calcular_media(nota_1, nota_2, nota_3)

    ranking_media(media, nome)

    inc_aprovado, inc_reprovado = situacao(media)
    aprovados += inc_aprovado
    reprovados += inc_reprovado
    

    media_turma += media
        
media_turma /= quantidade_alunos

print("Numero de aprovados {}".format(aprovados))
print("Numero de reprovados {}".format(reprovados))
print("Média da turma {}".format(media_turma))
print("Aluno maior nota: {}".format(aluno_maior_media))
print("Aluno menor Nota: {}".format(aluno_menor_media))