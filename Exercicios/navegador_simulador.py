# Classe Pilha (usada para histórico de voltar e avançar)
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

    def limpar(self):
        self.itens = []


# Classe Navegador
class Navegador:
    def __init__(self, pagina_inicial):
        self.historico_voltar = Pilha()
        self.historico_avancar = Pilha()
        self.pagina_atual = pagina_inicial
        print(f"Navegador iniciado em: {self.pagina_atual}")

    def visitar_pagina(self, url):
        self.historico_voltar.push(self.pagina_atual)
        self.pagina_atual = url
        self.historico_avancar.limpar()
        print(f"Visitando: {self.pagina_atual}")

    def voltar(self):
        if not self.historico_voltar.esta_vazia():
            self.historico_avancar.push(self.pagina_atual)
            self.pagina_atual = self.historico_voltar.pop()
        print(f"Voltando para: {self.pagina_atual}")

    def avancar(self):
        if not self.historico_avancar.esta_vazia():
            self.historico_voltar.push(self.pagina_atual)
            self.pagina_atual = self.historico_avancar.pop()
        print(f"Avançando para: {self.pagina_atual}")


# Testando o Navegador
if __name__ == "__main__":
    navegador = Navegador("inicio.com")

    navegador.visitar_pagina("pagina1.com")
    navegador.visitar_pagina("pagina2.com")
    navegador.visitar_pagina("pagina3.com")

    navegador.voltar()
    navegador.voltar()

    navegador.avancar()
    navegador.visitar_pagina("nova-pagina.com")

    navegador.voltar()



#por no terminal
python navegador_simulador.py
