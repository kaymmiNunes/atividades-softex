from abc import ABC, abstractmethod

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        """Retorna o valor da transação"""
        pass
    
    @abstractmethod
    def registrar(self, conta):
        """Aplica a transação em uma conta"""
        pass
