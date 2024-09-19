# Lista de contas
contas = ["2 + 2", "4 - 2", "2 * 2", "2 * 2", "4 / 2"]

# Função para calcular e imprimir uma conta por vez
def imprimir_contas(contas):
    for conta in contas:
        resultado = eval(conta)
        print(f"{conta} = {resultado}")

# Chamar a função para imprimir as contas
imprimir_contas(contas)
