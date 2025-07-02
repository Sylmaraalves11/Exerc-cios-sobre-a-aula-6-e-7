

# Classe que implementa uma pilha (estrutura LIFO)
class Pilha:
    def __init__(self):
        self.itens = []

    def push(self, item):
        self.itens.append(item)

    def pop(self):
        if not self.esta_vazia():
            return self.itens.pop()
        return None

    def esta_vazia(self):
        return len(self.itens) == 0


# Função que inverte uma string usando a classe Pilha
def inverter_string(texto):
    pilha = Pilha()

    # Empilhar cada caractere da string
    for caractere in texto:
        pilha.push(caractere)

    # Desempilhar para formar a string invertida
    texto_invertido = ''
    while not pilha.esta_vazia():
        texto_invertido += pilha.pop()

    return texto_invertido


# Execução principal
if __name__ == "__main__":
    entrada = input("Digite uma palavra para inverter: ")
    saida = inverter_string(entrada)
    print(f"Palavra invertida: {saida}")

#por no terminal
python pilha_inverter.py


