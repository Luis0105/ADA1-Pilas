class Pila:
    def __init__(self):
        self.elementos = []

    def vacia(self):
        return self.elementos == []

    def apilar(self, item):
        self.elementos.append(item)

    def desapilar(self):
        return self.elementos.pop()

    def elemento_superior(self):
        return self.elementos[-1] if not self.vacia() else None

    def tamaño(self):
        return len(self.elementos)

def hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mover disco 1 de {origen} a {destino}")
    else:
        hanoi(n - 1, origen, auxiliar, destino)
        print(f"Mover disco {n} de {origen} a {destino}")
        hanoi(n - 1, auxiliar, destino, origen)

hanoi(3, 'Torre 1', 'Torre 3', 'Torre 2')