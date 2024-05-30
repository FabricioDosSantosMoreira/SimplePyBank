#from src.app.interface import Interface

from datetime import date
from typing import List


# Classe base 'Cliente()' que irá extender outros tipos de clientes
class Cliente():

    def __init__(self, cep: str, nome: str, data_nascimento: date) -> None:
        
        self._contas: List = [] 

        self._cep: str = cep
        self._nome: str = nome
        self._data_nascimento: date = data_nascimento

    @classmethod
    def novo_cliente(cls, cep: str) -> 'Cliente':
        return cls(cep)
    
    def adicionar_conta(self, conta) -> None:
        self._contas.append(conta)
    
    def realizar_transacao(self, transacao, conta) -> None:

        qtd_transacoes_hoje = conta.historico.transacoes_do_dia()

        if qtd_transacoes_hoje >= conta.limite_transacoes:
            Interface.avisar(2, aviso="O número máximo de transacoes diárias já foi atingido. Volte amanhã!")
         
            return

        transacao.registrar(conta)


    @property
    def cep(self) -> str:
        return self._cep
    
    @property
    def contas(self) -> List:
        return self._contas

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def data_nascimento(self) -> date:
        return self._data_nascimento