import rpyc
import sys

if len(sys.argv) < 2:
    exit("Usage {} SERVER".format(sys.argv[0]))

server = sys.argv[1]
conn = rpyc.connect(server,18861)

# input do usuário
n = int(input("Digite um número para o tamanho de um vetor de elementos sequenciais: "))

# cria o vetor de 0 até n-1
vetor = list(range(n))

#mostra vetor criado aleatoriamente
print("Vetor criado: ", vetor)

# imprime o resultado
print(conn.root.sum_vector(vetor))