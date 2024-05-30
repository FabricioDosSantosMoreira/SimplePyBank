from app.Configs import *

from cartao.Cartao import Cartao

from datetime import date
from typing import Dict

from transacao.Transacao import Transferencia


# Extende a classe 'Cartao()'. Herança simples
class CartaoCredito(Cartao):
    
    def __init__(self, conta, limite: float) -> None:
        super().__init__(conta)

        self._limite = limite

        self._taxa_juros = TAXA_JUROS
        self._fatura: Dict[date, float] = {}

    def realizar_pagamento():

        #TODO:
        







    def calcular_juros(self, valor: float, taxa_juros_mensal: float, periodo: int) -> float:
        # NOTE: Periodo deve ser date.month

        return valor * taxa_juros_mensal * periodo

    def adicionar_valor_na_fatura(self, valor: float, periodo: int) -> None:
        # NOTE: Periodo deve ser date.month

        for data, total in self.fatura.items():

            if data.month == periodo:
                self.fatura[data] = total + valor

    def pagar_fatura(self, valor: float, periodo: int) -> float:
        resto: float = 0.0
        # NOTE: Periodo deve ser date.month

        for data, total in self.fatura.items():

            if data.month == periodo:       
                
                if valor >= total:
                    self.fatura[data] = 0
                    resto = total - valor

                else:
                    self.fatura[data] = total - valor

        return resto

    @property
    def fatura(self) -> Dict[date, float]:
        return self._fatura
    
    @fatura.setter
    def fatura(self, data: date, valor: float) -> None:  
        self._fatura[data] = valor

    @property
    def limite(self) -> float:
        return self._limite
    