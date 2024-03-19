class Pilha:
    def __init__(self):
        self._elementos = []

    def empilhar(self, item):
        self._elementos.append(item)

    def desempilhar(self):
        if not self.esta_vazia():
            return self._elementos.pop()

    def esta_vazia(self):
        return len(self._elementos) == 0


# Usando abstração de dados
pilha = Pilha()
pilha.empilhar("Python")
pilha.empilhar("C++")
pilha.empilhar("Teste")
print(pilha.desempilhar())  # C++
print(pilha.desempilhar())  # Python
print(pilha.desempilhar())
print(pilha.desempilhar())
