class Lampada:

    def __init__(self, ligada): # Método construtor
        self.ligada = ligada # Atributo de instância
        self.ligada = False # Atributo de instância

    def ligar(self): # Método de instância
        self.ligada = True
        return self.ligada
    
    def desligar(self): # Método de instância
        self.ligada = False
        return self.ligada
    
lampada = Lampada(True) 

print("Esse é o estado inicial da lâmpada:", lampada.ligada)
print("Lâmpada ligada:", lampada.ligar())
print("Lâmpada desligada:", lampada.desligar())
