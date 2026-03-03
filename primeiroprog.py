quantidade_alunos = int(input("Quantos alunos? "))
i = 0
aprovados = 0
reprovados = 0
media_turma = 0
aluno_maior_media = ""
aluno_menor_media = ""

while quantidade_alunos != i:
    i+=1
    notas = []
    maior_media = 0
    menor_media = 10

    nome = input("Nome: ")
    for a in range(1,4):
        notas.append(int(input("Notas: ")))

    media = (notas[0] + notas[1] + notas[2])/3
    
    media_turma += media
    
    print("Média do aluno {}".format(media))
    if media >= 7:
        print("Aprovado")
        aprovados += 1
    elif 5<= media < 7:
        print("Prova Final")
    else:
        print("Reprovado")
        reprovados += 1
    
    if quantidade_alunos == 1:
        aluno_menor_media = aluno_maior_media = nome
    elif media < menor_media:
        aluno_menor_media = nome
    else:
        aluno_maior_media = nome
        

media_turma/=quantidade_alunos

print("Numero de aprovados {}".format(aprovados))
print("Numero de reprovados {}".format(reprovados))
print("Média da turma {}".format(media_turma))
print("Aluno com maior media {}".format(aluno_maior_media))
print("Aluno com menor media {}".format(aluno_menor_media))