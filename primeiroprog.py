quantidade_alunos = int(input("Quantos alunos? "))
i = 0
aprovados = 0
reprovados = 0
media_turma = 0
maior_media = None
menor_media = None
aluno_maior_media = ""
aluno_menor_media = ""

def calcular_media(n1, n2, n3, nome_aluno) -> int:
    global media_turma
    media = (n1+n2+n3)/3
    ranking_media(media, nome_aluno)
    media_turma += media
    return media

def situacao(media:int):
    global aprovados
    global reprovados
    if media >= 7:
        print("Aprovado")
        aprovados += 1
    elif 5 <= media < 7:
        print("Prova Final")
    else:
        print("Reprovado")
        reprovados += 1

def calcular_media_turma():
    global quantidade_alunos
    global media_turma
    media_turma /= quantidade_alunos

def ranking_media(media, nome_aluno):
    global aluno_maior_media
    global aluno_menor_media
    global maior_media
    global menor_media
    if maior_media is None:
        aluno_maior_media = nome_aluno
        aluno_menor_media = nome_aluno
        maior_media = media
        menor_media = media
    elif media > maior_media:
        aluno_maior_media = nome_aluno
        maior_media = media
    elif media < menor_media:
        aluno_menor_media= nome_aluno
        menor_media = media


while quantidade_alunos != i:
    i+=1
    notas = []

    nome = input("Nome: ")
    nota_1 = int(input("Notas: "))
    nota_2 = int(input("Notas: "))
    nota_3 = int(input("Notas: "))

    situacao(calcular_media(nota_1, nota_2, nota_3, nome))

    if i == quantidade_alunos:
        calcular_media_turma()

print("Numero de aprovados {}".format(aprovados))
print("Numero de reprovados {}".format(reprovados))
print("Média da turma {}".format(media_turma))
print("Aluno maior nota: {}".format(aluno_maior_media))
print("Aluno menor Nota: {}".format(aluno_menor_media))