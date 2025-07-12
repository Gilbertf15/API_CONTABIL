from fastapi import APIRouter
from operations.operation import OperationsContabil


class RouterContabil(APIRouter):
    def __init__(self, prefix = "calculos"):
        super().__init__(prefix=prefix,)


routercontabil = RouterContabil()

@routercontabil.post("/juros_simples/{c}/{i}/{t}")
async def rota_juros_simples(c: int | float, i: int | float, t: int | float):
    """_summary_

    Args:
        c (int | float): _description_
        i (int | float): _description_
        t (int | float): _description_

    Returns:
        _type_: _description_
    """
    
    resultado_juros_simples = await OperationsContabil.juros_simples(c, i, t)
    return resultado_juros_simples


@routercontabil.post("/juros_compostos/{c}/{i}/{t}")
async def rota_juros_compostos(c: int | float, i: int | float, t: int | float):
    """_summary_

    Args:
        c (int | float): _description_
        i (int | float): _description_
        t (int | float): _description_

    Returns:
        _type_: _description_
    """
    resultado_juros_compostos = await OperationsContabil.juros_compostos(c, i, t)
    return resultado_juros_compostos


@routercontabil.post("/valor_presente/{VF}/{i}/{n}")
async def rota_valor_presente(VF: int | float, i: int | float, n: int | float):
    """_summary_

    Args:
        VF (int | float): _description_
        i (int | float): _description_
        n (int | float): _description_

    Returns:
        _type_: _description_
    """
    resultado_valor_presente = await OperationsContabil.valor_presente(VF, i, n)
    return resultado_valor_presente

@routercontabil.post("/valor_futuro/{VP}/{i}/{n}")
async def rota_valor_futuro(VP: int | float, i: int | float, n: int | float ):
    """_summary_

    Args:
        VP (int | float): _description_
        i (int | float): _description_
        n (int | float): _description_

    Returns:
        _type_: _description_
    """
    resultado_valor_futuro = await OperationsContabil.valor_futuro(VP, i, n)
    return resultado_valor_futuro

@routercontabil.post("/margem_de_lucro/{lucro}/{receita}")
async def rota_margem_lucro(lucro: int | float, receita: int | float):
    """_summary_

    Args:
        lucro (int | float): _description_
        receita (int | float): _description_

    Returns:
        _type_: _description_
    """
    resultado_margem_lucro = await OperationsContabil.margem_de_lucro(lucro, receita)
    return resultado_margem_lucro

@routercontabil.post("/custo_total/{VF}/{custo_v}")
async def rota_custo_total(CF: int | float, custo_v: int | float):
    """_summary_

    Args:
        CF (int | float): _description_
        custo_v (int | float): _description_

    Returns:
        _type_: _description_
    """
    resultado_custo_total = await OperationsContabil.custo_total(CF, custo_v)
    return resultado_custo_total

@routercontabil.post("/depreciacao_linear/{valor_aquisitivo}/{valor_residual}")
async def rota_depreciacao_linear(valor_aquisitivo: int | float, valor_residual:int | float):
    """_summary_

    Args:
        valor_aquisitivo (int | float): _description_
        valor_residual (int | float): _description_

    Returns:
        _type_: _description_
    """
    resultado_depreciacao_linear = await OperationsContabil.depreciacao_linear(valor_aquisitivo, valor_residual)
    return resultado_depreciacao_linear

@routercontabil.post("/ponto_equilibrio/{cf}/{pv}/{custo_v}")
async def rota_ponto_equilibrio(cf: int | float, pv: int | float, custo_v: int | float):
    """_summary_

    Args:
        cf (int | float): _description_
        pv (int | float): _description_
        custo_v (int | float): _description_

    Returns:
        _type_: _description_
    """
    resultado_ponto_equilibrio = await OperationsContabil.ponto_de_equilibrio(cf, pv, custo_v)
    return resultado_ponto_equilibrio

@routercontabil.post("/liquidez_corrente/{ativo_circulante}/{passivo_circulante}")
async def rota_liquidez_corrente(ativo_circulante: int | float, passivo_circulante: int | float):
    """_summary_

    Args:
        ativo_circulante (int | float): _description_
        passivo_circulante (int | float): _description_

    Returns:
        _type_: _description_
    """
    resultado_liquidez_corrente = await OperationsContabil.liquidez_corrente(ativo_circulante, passivo_circulante)
    return resultado_liquidez_corrente