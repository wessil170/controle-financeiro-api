from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator
from datetime import date
from decimal import Decimal
from typing import List

app = FastAPI(title="Controle Financeiro API")

class Lancamento(BaseModel):
    id: int
    tipo: str
    valor: Decimal
    data: date

    @field_validator("tipo")
    def validar_tipo(cls, v):
        if v not in ["receita", "despesa"]:
            raise ValueError("tipo deve ser 'receita' ou 'despesa'")
        return v


class LancamentoUpdate(BaseModel):
    tipo: str
    valor: Decimal
    data: date

lancamentos: List[Lancamento] = [
    Lancamento(id=1, tipo="receita", valor=3500, data="2026-01-01"),
    Lancamento(id=2, tipo="despesa", valor=1200, data="2026-01-05"),
    Lancamento(id=3, tipo="despesa", valor=450, data="2026-01-08"),
]

@app.get("/lancamentos")
def listar_lancamentos():
    return lancamentos


@app.post("/lancamentos")
def criar_lancamento(lancamento: Lancamento):
    lancamentos.append(lancamento)
    return lancamento


@app.put("/lancamentos/{id}")
def atualizar_lancamento(id: int, dados: LancamentoUpdate):
    for index, lancamento in enumerate(lancamentos):
        if lancamento.id == id:
            lancamentos[index] = Lancamento(
                id=id,
                **dados.dict()
            )
            return lancamentos[index]

    raise HTTPException(status_code=404, detail="Lançamento não encontrado")


@app.delete("/lancamentos/{id}")
def deletar_lancamento(id: int):
    for index, lancamento in enumerate(lancamentos):
        if lancamento.id == id:
            lancamentos.pop(index)
            return {"mensagem": "Lançamento removido com sucesso"}

    raise HTTPException(status_code=404, detail="Lançamento não encontrado")
