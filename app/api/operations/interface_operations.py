from abc import ABC, abstractmethod

class Interface(ABC):

    @abstractmethod
    async def juros_simples():
        raise NotImplementedError("Método juros simples não implementado")

    @abstractmethod
    def juros_compostos():
        raise NotImplementedError("Método juros compostos não implementado")

    @abstractmethod
    def desconto_simples():
        raise NotImplementedError("Método desconto simples não implementado")

    @abstractmethod
    def valor_presente():
        raise NotImplementedError("Método valor presente não implementado")

    @abstractmethod
    def valor_futuro():
        raise NotImplementedError("Método valor futuro não implementado")

    @abstractmethod
    def margem_de_lucro():
        raise NotImplementedError("Método margem de luvro não implementado")

    @abstractmethod
    def custo_total():
        raise NotImplementedError("Método custo total não implementado")
    
    @abstractmethod
    def depreciacao_linear():
        raise NotImplementedError("Método depreciação linear não implementado")
    
    @abstractmethod
    async def ponto_de_equilibrio():
        raise NotImplementedError("Método ponto de equilibrio não implementado")
    
    @abstractmethod
    def liquidez_corrente():
        raise NotImplementedError("Método liquidez corrente não implementado")