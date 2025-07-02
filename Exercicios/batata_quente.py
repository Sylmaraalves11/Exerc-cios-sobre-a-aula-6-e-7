from collections import deque

# Função principal do jogo da batata quente
def simular_batata_quente(lista_nomes, num_passes):
    fila = deque(lista_nomes)  # deque é uma fila eficiente em Python

    while len(fila) > 1:
        # Passa a batata num_passes vezes
        for _ in range(num_passes):
            pessoa = fila.popleft()
            fila.append(pessoa)  # volta pro fim da fila
            print(f"Passando a batata... {pessoa}")

        # A pessoa que se queimou sai da fila
        queimado = fila.popleft()
        print(f"{queimado} saiu do jogo!")

    vencedor = fila[0]
    print(f"\n🎉 O vencedor é: {vencedor}")
    return vencedor


# Testando o jogo
if __name__ == "__main__":
    nomes = ["Ana", "Bia", "Carlos", "Dani", "Eva"]
    num_passes = 7
    simular_batata_quente(nomes, num_passes)
