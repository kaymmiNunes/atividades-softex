class Lampada:

    def __init__(self, ligada):
        self.ligada = ligada
        self.ligada = False

    def ligar(self):
        self.ligada = True
        return self.ligada
    
    def desligar(self):
        self.ligada = False
        return self.ligada
    
lampada = Lampada(True)

print("Esse é o estado inicial da lâmpada:", lampada.ligada)
print("Lâmpada ligada:", lampada.ligar())
print("Lâmpada desligada:", lampada.desligar())
