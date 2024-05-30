from cartao.Cartao import Cartao

from transacao.Transacao import Transferencia

# Extende a classe 'Cartao()'. Herança simples
class CartaoDebito(Cartao):

    def __init__(self, conta) -> None:
        super().__init__(conta)

    def realizar_pagamento(self, valor: float, destinatario: str):

        # TODO: O destinatário tem que receber o dinheiro né
        transferencia = Transferencia(valor=valor, destinatario=destinatario)
        transferencia.registrar(self)
        
        # A ideia de quando fosse realizar um pagamento o cliente deveria escolhar 
        # um dos cartoes de credito ou debito, o de debito usa o saldo da conta
        # ja o de credito poderia parcelar e adicionar juros

        # TODO: adicionar no CARTAO DE CREDITO na fatura o valor da transferencia