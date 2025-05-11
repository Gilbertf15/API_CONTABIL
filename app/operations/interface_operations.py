from abc import ABC, abstractmethod

class Interface(ABC):


    @abstractmethod
    def juros_simples(self):
        raise NotImplementedError("Método juros simples não implementado")