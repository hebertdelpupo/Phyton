quantidade_minima = int(input("Informe a quantidade mínima do estoque: "))
quantidade_maxima = int(input("Informe a quantidade máxima do estoque: "))

estoque_medio = (quantidade_minima + quantidade_maxima) / 2
print("O estoque médio é {0}".format(estoque_medio))
