from classes.historico.Historico import HistoricoConta
from app.Interface import Interface
from classes.cartao.Cartao import Cartao
from app.Configs import *

from typing import List
import random

class Conta():

    def __init__(self, cliente, ID: int) -> None:
        
        self._ID: int = ID

        self._historico = HistoricoConta()

        self._cartoes: List[Cartao]
        self._cliente = cliente

        self._numero_transacoes: int = 0
        self._saldo: float = 0.0
        self._agencia: str 

        self.carregar_configuracoes()

    @classmethod 
    def nova_conta(cls, cliente, ID: int) -> 'Conta':
        return cls(cliente, ID)
    
    def carregar_configuracoes(self) -> None:

        agencia = self.criar_agencia(agencias_disponiveis)
        self.agencia = agencia

    def criar_agencia(self, agencias: List[str], indice: int = None) -> None:

        if not indice:
            # Cria um índice aleatório para obter uma agência aleatória
            indice = random.randint(0, len(agencias))

        return agencias[indice]

    def adicionar_cartao(self, cartao: Cartao) -> None:
        self.cartoes.append(cartao)
    
    def sacar(self, valor: float) -> bool:
        sucesso: bool = False

        if valor > self.saldo:
            Interface.avisar(2, aviso="A operação falhou. Você não possui saldo suficiente!")
        
        elif valor <= 0:
            Interface.avisar(2, aviso="A operação falhou. O valor informado é inválido!")

        else:
            self.transacoes += 1
            self.saldo -= valor
            Interface.avisar(1, aviso=f"Saque de R$ {valor:.2f} realizado com sucesso!")

            sucesso = True

        return sucesso
    
    def depositar(self, valor):
        sucesso: bool = False

        if valor <= 0:  
            Interface.avisar(2, aviso="A operação falhou. O valor informado é inválido!")
        
        else:
            self.saldo += valor
            Interface.avisar(1, aviso=f"Depósito de R$ {valor:.2f} realizado com sucesso!")

            self.transacoes += 1

            sucesso = True

        return sucesso
    
    def transferir(self, valor: float) -> bool:

        # TODO: ta mas e se é credito??  nao pode remover o saldo da conta
        sucesso: bool = False

        if valor <= 0:
            Interface.avisar(2, aviso="A operação falhou. O valor informado é inválido!")

        elif valor> self.saldo:
            Interface.avisar(2, aviso="A operação falhou. Você não possui saldo suficiente!")

        else:
            self.saldo -= valor
            Interface.avisar(1, aviso=f"Transferência de R$ {valor:.2f} é possível!")

            sucesso = True

        return sucesso

    @property
    def historico(self) -> HistoricoConta:
        return self._historico
    
    @property
    def cartoes(self) -> List[Cartao]:
        return self._cartoes
    
    @property
    def cliente(self):
        return self._cliente

    @property
    def ID(self):
        return self._ID
    
    # Número transações
    @property
    def transacoes(self) -> int:
        return self._numero_transacoes

    @transacoes.setter
    def numero_transacoes(self, valor: int) -> None:
        self._numero_transacoes = valor

    # Saldo
    @property
    def saldo(self) -> float:
        return self._saldo

    @saldo.setter
    def saldo(self, valor: int) -> None:
        self._numero__saldotransacoes = valor

    # Agência 
    @property
    def agencia(self) -> str:
        return self._agencia
    
    @agencia.setter
    def agencia(self, valor: str) -> None:
        self._agencia = valor



