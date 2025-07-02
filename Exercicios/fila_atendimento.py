# Classe Fila com lista encadeada simples (usando lista para facilitar visualização)
class Fila:
    def __init__(self):
        self.itens = []

    def enqueue(self, item):
        self.itens.append(item)  # adiciona no final

    def dequeue(self):
        if not self.esta_vazia():
            return self.itens.pop(0)  # remove do início
        return None

    def esta_vazia(self):
        return len(self.itens) == 0

    def mostrar_fila(self):
        print("Fila atual:", " -> ".join(self.itens) if self.itens else "vazia")


# Adiciona um novo cliente à fila
def novo_cliente(fila, nome_cliente):
    fila.enqueue(nome_cliente)
    print(f"Novo cliente adicionado: {nome_cliente}")
    fila.mostrar_fila()


# Atende o próximo cliente da fila
def atender_cliente(fila):
    if not fila.esta_vazia():
        cliente = fila.dequeue()
        print(f"Atendendo cliente: {cliente}")
    else:
        print("Nenhum cliente para atender.")
    fila.mostrar_fila()


# Simulação do atendimento
def simular_atendimento():
    fila = Fila()

    # Adiciona 3 clientes
    novo_cliente(fila, "João")
    novo_cliente(fila, "Maria")
    novo_cliente(fila, "Carlos")

    # Atende 1 cliente
    atender_cliente(fila)

    # Adiciona mais 1 cliente
    novo_cliente(fila, "Ana")

    # Atende o restante
    while not fila.esta_vazia():
        atender_cliente(fila)


# Executa a simulação
if __name__ == "__main__":
    simular_atendimento()




#executar o script
python fila_atendimento.py