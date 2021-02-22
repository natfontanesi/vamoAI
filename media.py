'''Uma professora deseja desenvolver um sistema para automatizar
seu trabalho. Ela precisa criar uma solução onde seus alunos
consigam inserir suas notas (seja a média geral de todas as
matérias ou a média de uma única disciplina), receber a média, e
saber sua situação (aprovação, reprovação ou recuperação).'''

def calcula_media(soma,tamanho):
    soma_das_notas=sum(soma)
    soma_das_notas=soma_das_notas/tamanho
    return soma_das_notas

media=int(input("Voce quer saber sua média geral(1) ou média da mesma matéria(2) "))

if(media == 1):
    tamanho= int(input("Quantas notas você vai inserir? "))
    soma=[]
    for i in range(0,tamanho):
        soma.append(float(input("Digite sua nota {}: ".format(i))))

elif(media == 2):
    tamanho = 3
    soma=[]
    for i in range(0,tamanho):
        soma.append(float(input("Digite sua nota {}: ".format(i)))) 
else:
    print("Número inválido")
soma=calcula_media(soma,tamanho)
if(soma>7)and(soma<=10):
    print("Você está aprovado! Sua nota foi {:.2f}".format(soma))
elif(soma<7)and(soma>5):
    print("Você está em recuperação! Sua nota foi {:.2f}".format(soma))
elif(soma<5)and(soma>0):
    print("Você está reprovado! Sua nota foi {:.2f}".format(soma))