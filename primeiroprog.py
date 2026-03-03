quantidade_alunos = int(input("Quantos alunos? "))
i = 0
aprovados = 0
reprovados = 0
media_turma = 0

def calcular_media(n1, n2, n3) -> int:
    media = (n1+n2+n3)/3
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

def calcular_media_turma(media):
    global quantidade_alunos
    global media_turma
    media_turma += media
    media_turma /= quantidade_alunos
    return media_turma

while quantidade_alunos != i:
    i+=1
    notas = []

    nome = input("Nome: ")
    nota_1 = int(input("Notas: "))
    nota_2 = int(input("Notas: "))
    nota_3 = int(input("Notas: "))

    calcular_media_turma(calcular_media(nota_1, nota_2, nota_3))
    situacao(calcular_media(nota_1, nota_2, nota_3))
    


print("Numero de aprovados {}".format(aprovados))
print("Numero de reprovados {}".format(reprovados))
print("Média da turma {}".format(media_turma))