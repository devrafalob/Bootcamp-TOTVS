quantidade_alunos = int(input("Quantos alunos? "))
i = 0
aprovados = 0
reprovados = 0
media_turma = 0
maior_media = None
menor_media = None
aluno_maior_media = ""
aluno_menor_media = ""

#retirar global das funções e que cada função retorne valores
def calcular_media(n1, n2, n3) -> float:
    media = (n1+n2+n3)/3
    return media

def somatorio_media(media)-> float: 
    media_turma += media
    return media_turma

def situacao(media) -> str:
    if media >= 7:
        return "Aprovado"
    elif 5 <= media < 7:
        return "Prova Final"
    else:
        return "Reprovado"
    
def contador_situaçao(situacao, contador):
    if situacao == "Aprovado":
        return contador + 1
    elif situacao == "Reprovado":
        return contador + 1

def calcular_media_turma()->float:
    media_turma /= quantidade_alunos
    return media_turma

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


for i in range(quantidade_alunos):
    notas = []

    nome = input("Nome: ")
    nota_1 = int(input("Notas: "))
    nota_2 = int(input("Notas: "))
    nota_3 = int(input("Notas: "))

    media = calcular_media(nota_1, nota_2, nota_3)
    ranking_media(media, nome)
    contador_situaçao(situacao(media))
    somatorio_media(media)

    if range == quantidade_alunos:
        calcular_media_turma()

print("Numero de aprovados {}".format(aprovados))
print("Numero de reprovados {}".format(reprovados))
print("Média da turma {}".format(media_turma))
print("Aluno maior nota: {}".format(aluno_maior_media))
print("Aluno menor Nota: {}".format(aluno_menor_media))