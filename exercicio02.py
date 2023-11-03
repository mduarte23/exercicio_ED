def media(n):
    if n >= 6:
        return "Aprovado"
    elif n >= 4:
        return "Verificação Suplementar"
    else:
        return "Reprovado"
    
nome = input("Digite o nome do aluno: ")
nota = float(input("Digite a nota: "))
situacao = media(nota)

print(f"A nota do aluno {nome} está {situacao}")