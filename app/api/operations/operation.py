from interface_operations import Interface

class OperationsContabil(Interface):
    """
    Args:
        Interface (_type_): _description_
    """
    
    @staticmethod
    async def juros_simples(c:int | float, i:int | float, t:int | float) -> int | float | str:
        """_summary_

        Args:
            c (int | float): _description_
            i (int | float): _description_
            t (int | float): _description_

        Returns:
            int | float | str: _description_
        """
        try:
            result = (c * (i / 100) * t)
            return result
        
        except Exception as e:
            return "error calculo(juros simpes)", e
        
    @staticmethod
    async def juros_compostos(c:int | float, i: int| float, t: int | float) -> int | float | str:
        """_summary_

        Args:
            c (int | float): _description_
            i (int | float): _description_
            t (int | float): _description_

        Returns:
            int | float | str: _description_
        """
        try:
            result = c * (1 + (i / 100)) ** t
            return result
        
        except Exception as e:
            return "error calculo (juros compostos)", e
        

    @staticmethod
    async def desconto_simples(N: int | float, i: int | float, t :int | float) -> int | float | str:
        """_summary_

        Args:
            N (int | float): _description_
            i (int | float): _description_
            t (int | float): _description_

        Returns:
            int | float | str: _description_
        """
        try:
            result = N * (i / 100) * t
            return result
        
        except Exception as e:
            return "erros calculo (desconto simples)", e


    @staticmethod
    async def valor_presente(VF:int | float, i: int | float , n: int | float) -> int | float | str:
        """_summary_

        Args:
            VF (int | float): _description_
            i (int | float): _description_
            n (int | float): _description_

        Returns:
            int | float | str: _description_
        """
        try:
            result = VF / (1 + (i / 100)) ** n

            return result
        except Exception as e:
            return "Error calculo (valor presente)", e
        

    @staticmethod
    async def valor_futuro(VP: int | float, i: int | float, n: int | float) -> int | float | str:
        """_summary_

        Args:
            VP (int | float): _description_
            i (int | float): _description_
            n (int | float): _description_

        Returns:
            int | float | str: _description_
        """
        try:
            result = VP * (1 + (i / 100)) ** n
            return result
        except Exception as e:
            return "Error calculo (valor futuro)", e
        
    @staticmethod
    async def margem_de_lucro(lucro: int | float, receita: int | float) -> int | float | str:
        """_summary_

        Args:
            lucro (int | float): _description_
            receita (int | float): _description_

        Returns:
            int | float | str: _description_
        """
        try:
            margem = (lucro / receita) * 100
            return margem
        except Exception as e:
            return "Error calculo (margem de lucro)", e
        
    @staticmethod
    async def custo_total(CF: int | float, custo_v: int | float) -> int | float | str:
        """_summary_

        Args:
            CF (int | float): _description_
            custo_v (int | float): _description_

        Returns:
            int | float | str: _description_
        """
        try:
            ct = CF + custo_v
            return ct 
        except Exception as e:
            return "Error calculo (custo total)", e
        

    @staticmethod 
    async def depreciacao_linear(valor_aquisicao:int | float, valor_residual: int | float, vida_util: int) -> int | float | str:
        """_summary_

        Args:
            valor_aquisicao (int | float): _description_
            valor_residual (int | float): _description_
            vida_util (int): _description_

        Returns:
            int | float | str: _description_
        """
        try:
            depreciacao = (valor_aquisicao - valor_residual) / vida_util
            return depreciacao
        
        except Exception as e:
            "Error calculo (depreciacao linear)", e


    @staticmethod
    async def ponto_de_equilibrio(cf: int | float, pv: int | float, custo_v: int | float ) -> int | float | str:
        """_summary_

        Args:
            cf (int | float): _description_
            pv (int | float): _description_
            custo_v (int | float): _description_

        Returns:
            int | float | str: _description_
        """
        try:
            ponto_equilibrio = cf / (pv - custo_v)
            return ponto_equilibrio
        except Exception as e:
            "Error calculo (ponto de equilibrio)", e


    @staticmethod
    async def liquidez_corrente(ativo_circulante: int | float, passivo_circulante: int | float) -> int | float | str:
        """_summary_

        Args:
            ativo_circulante (int | float): _description_
            passivo_circulante (int | float): _description_

        Returns:
            int | float | str: _description_
        """
        try:
            liquidez = ativo_circulante / passivo_circulante
            return liquidez
        
        except Exception as e:
            return "Error calculo (liquidez corrente)", e