from abc import ABC, abstractmethod

class Interface(ABC):

    @abstractmethod
    def juros_simples(self):
        raise NotImplementedError("Método juros simples não implementado")

    @abstractmethod
    def juros_compostos(self):
        raise NotImplementedError("Método juros compostos não implementado")

    @abstractmethod
    def desconto_simples(self):
        raise NotImplementedError("Método desconto simples não implementado")

    @abstractmethod
    def valor_presente(self):
        raise NotImplementedError("Método valor presente não implementado")

    @abstractmethod
    def valor_futuro(self):
        raise NotImplementedError("Método valor futuro não implementado")

    @abstractmethod
    def margem_de_lucro(self):
        raise NotImplementedError("Método margem de luvro não implementado")

    @abstractmethod
    def custo_total(self):
        raise NotImplementedError("Método custo total não implementado")
    
    @abstractmethod
    def depreciacao_linear(self):
        raise NotImplementedError("Método depreciação linear não implementado")
    
    @abstractmethod
    def ponto_de_equilibrio(self):
        raise NotImplementedError("Método ponto de equilibrio não implementado")
    
    @abstractmethod
    def liquidez_corrente(self):
        raise NotImplementedError("Método liquidez corrente não implementado")