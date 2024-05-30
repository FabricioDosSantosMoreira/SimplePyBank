from app.Configs import *

from card.Card import Card

from datetime import date
from typing import Dict

from transaction.Transaction import Transfer
from app.Configs import Configs

# Extende a classe 'Cartao()'. Herança simples
class CreditCard(Card):
    
    def __init__(self, account, limit: float) -> None:
        super().__init__(account)
        self.configs = Configs()

        self._limit= limit
        self._interest_rate = self.configs.interest_rate
        self._invoice: Dict[date, float] = {}


    def realizar_pagamento():

        #TODO:
        print("IMPLEMENT ME!!!!!!!!!!!!!")
        

    def calculate_interest(self, value: float, monthly_interest_rate: float, period: date) -> float:

        return value * monthly_interest_rate * period.month

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
    def invoice(self) -> Dict[date, float]:
        return self._invoice
    
    @invoice.setter
    def fatura(self, date: date, value: float) -> None:  
        self._invoice[date] = value

    @property
    def limit(self) -> float:
        return self._limit
    
    @limit.setter
    def limit(self, value: float) -> None:
        self._limit = value
    

