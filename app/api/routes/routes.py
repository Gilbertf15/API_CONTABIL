from fastapi import APIRouter
from operations.operation import OperationsContabil


class RouterContabil(APIRouter):
    def __init__(self, prefix = "calculos"):
        super().__init__(prefix=prefix,)


routercontabil = RouterContabil()

@routercontabil.post("/juros_simples/{c}/{i}/{t}")
async def rota_juros_simples(c: int | float, i: int | float, t: int | float):
    
    resultado_juros_simples = await OperationsContabil.juros_simples(c, i, t)
    return resultado_juros_simples


@routercontabil.post("/juros_compostos/{c}/{i}/{t}")
async def rota_juros_compostos(c: int | float, i: int | float, t: int | float):
    
    resultado_juros_compostos = await OperationsContabil.juros_compostos(c, i, t)
    return resultado_juros_compostos


@routercontabil.post("/valor_presente/{VF}/{i}/{n}")
async def rota_valor_presente(VF: int | float, i: int | float, n: int | float):
    
    resultado_valor_presente = await OperationsContabil.valor_presente(VF, i, n)
    return resultado_valor_presente

@routercontabil.post("/valor_futuro/{VP}/{i}/{n}")
async def rota_valor_futuro(VP: int | float, i: int | float, n: int | float ):
    resultado_valor_futuro = await OperationsContabil.valor_futuro(VP, i, n)
    return resultado_valor_futuro