from datetime import datetime
import pytz
from classes.transacao.Transacao import Transacao


from typing import Generator, List


class Historico():

    def __init__(self) -> None:
        self._transacoes: List[Transacao]

    def gerador_relatorio(self, tipo_transacao = None):

        for transacao in self.transacoes:

            if (tipo_transacao is None or transacao['tipo'].lower() == tipo_transacao.lower()):
                
                yield transacao

    @property
    def transacoes(self) -> List:
        return self._transacoes


# O histórico de um determinado cartão
class HistoricoCartao(Historico):

    def __init__(self) -> None:
        super().__init__()

    def adicionar_transacao(self, transacao: Transacao, cartao, identificador: str = None) -> None:
        # O identificador teóricamente seria um cpf, cnpj ou matricula estudante

        destinatario = "você" if identificador is None else identificador

        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now(pytz.timezone("UTC")),
                "cartao": cartao.numero,
                "PARA QUEM???": destinatario
            }
        )


# O histórico da conta e todos os cartoes
class HistoricoConta(Historico):
    
    def __init__(self) -> None:
        super().__init__()

    def adicionar_transacao(self, transacao: Transacao, conta) -> None:
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now(pytz.timezone("UTC")),
                "cartao": conta.cliente
            }
        )
