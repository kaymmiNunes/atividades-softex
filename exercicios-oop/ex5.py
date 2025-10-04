'''Exercício 5: Herança em Múltiplos Níveis (Hierarquia)
Crie uma hierarquia de classes de três níveis:
1. DispositivoEletronico (Classe Base com ligar() e desligar()).
2. Computador (Herda de DispositivoEletronico, adiciona instalar_software()).
3. Notebook (Herda de Computador, adiciona verificar_bateria()).
Crie uma instância de Notebook e chame um método de cada nível de herança.'''

class DispositivoEletronico:

    def __init__(self):
         pass

    def ligar(self):
        return print("Dispositivo ligado.")
    
    def desligar(self):
        return print("Dispositivo desligado.")
    
class Computador(DispositivoEletronico):

    def __init__(self):
        super().__init__()

    def instalar_software(self):
        return print("Software instalado.")
      
class Notebook(Computador):
    
    def __init__(self):
        super().__init__()

    def verificar_bateria(self):
        return print("Bateria em 100%.")
      
notebook = Notebook()

notebook.ligar()
notebook.desligar()
notebook.instalar_software()
notebook.verificar_bateria()