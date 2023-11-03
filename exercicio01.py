import math

def combinacao (m,n):
    resultado = math.factorial(n)/(math.factorial(m)*(math.factorial(n-m)))
    return resultado
            

alunos = int(input("Informe a quantidade de alunos da turma: "))
grupo = int(input("Informe a quantidade de alunos no primeiro grupo: "))

combinacoes = combinacao(grupo, alunos)

print(f"O número de combinaçoes possíveis é {combinacoes}")