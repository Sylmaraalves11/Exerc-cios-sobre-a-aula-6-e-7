class FilaDePrioridade:
    def __init__(self):
        self.fila = []

    def enqueue(self, dado, prioridade):
        item = (prioridade, dado)
        inserido = False

        for i in range(len(self.fila)):
            if prioridade < self.fila[i][0]:
                self.fila.insert(i, item)
                inserido = True
                break

        if not inserido:
            self.fila.append(item)

        print(f"📥 Adicionado: '{dado}' com prioridade {prioridade}")

    def dequeue(self):
        if self.fila:
            prioridade, dado = self.fila.pop(0)
            print(f"📤 Removido: '{dado}' com prioridade {prioridade}")
            return dado
        else:
            print("⚠️ A fila está vazia.")
            return None

    def mostrar_fila(self):
        print("📄 Fila atual:")
        for prioridade, dado in self.fila:
            print(f"  - {dado} (prioridade {prioridade})")


# Simulação do exemplo
if __name__ == "__main__":
    fila = FilaDePrioridade()
    
    fila.enqueue("Relatório Urgente", 1)
    fila.enqueue("Documento Normal", 5)
    fila.enqueue("E-mail Rápido", 2)

    fila.mostrar_fila()

    print("\n➡️ Iniciando remoção da fila...")
    fila.dequeue()
    fila.mostrar_fila()

#por no terminal
python fila_prioridade.py
