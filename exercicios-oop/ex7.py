'''Exercício 7: Múltiplas Classes Abstratas (Mixins Conceituais)
Crie uma classe base abstrata Percurso com um método abstrato tempo_estimado(). Crie
uma segunda classe base abstrata Cobranca com um método abstrato calcular_tarifa().
Crie uma classe concreta Taxi que herda (e implementa) ambas as classes abstratas,
implementando os métodos de forma coerente.'''

from abc import ABC, abstractmethod

class Percurso(ABC):

    def __init__(self, distancia_km):
        self.distancia_km = distancia_km
        
    @abstractmethod
    def tempo_estimado(self):
        pass

class Cobranca(ABC):
    @abstractmethod
    def calcular_tarifa(self):
        pass
        
class Taxi(Percurso, Cobranca):

    def __init__(self, distancia_km):
        super().__init__(distancia_km)

    def tempo_estimado(self):
        return print(f"Tempo estimado para {self.distancia_km} km: {self.distancia_km} minutos") # Supondo 1 km = 1 minuto

    def calcular_tarifa(self):
        return print(f"Tarifa para {self.distancia_km} km: R$ {self.distancia_km * 2.5:.2f}".replace(".", ",")) # Exemplo: R$2,5 por km

taxi = Taxi(15) # 15 km

taxi.tempo_estimado()
taxi.calcular_tarifa()



