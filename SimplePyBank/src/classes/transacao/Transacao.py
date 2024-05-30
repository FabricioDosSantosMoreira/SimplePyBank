from abc import ABC, abstractmethod


# Classe abstrata que herda as funcionalidades do módulo ABC (Abstract Base Classes)
class Transacao(ABC):

    _valor: float 

    @property
    @abstractmethod
    def valor(self) -> float:
        return self._valor

    @valor.setter
    def valor(self, valor: float) -> None:
        self._valor = valor

    @abstractmethod
    def registrar(self, conta) -> None:
        pass


# Extende a classe 'Transacao()'. Herança simples
class Deposito(Transacao):

    def __init__(self, valor: float) -> None:
        self.valor = valor

    def registrar(self, conta) -> None:

        sucesso_transacao: bool = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self, conta)


# Extende a classe 'Transacao()'. Herança simples
class Saque(Transacao):

    def __init__(self, valor: float) -> None:
        self.valor = valor

    def registrar(self, conta) -> None:

        sucesso_transacao: bool = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self, conta)


# Extende a classe 'Transacao()'. Herança simples
class Transferencia(Transacao):
    # NOTE: A transferência só é possivel ser feita por um cartão de crédito ou débito

    def __init__(self, valor: float, destinatario: str) -> None:
        self.valor = valor
        self.destinatario = destinatario

    def registrar(self, cartao) -> None:
        
        sucesso_transacao: bool = cartao.conta.transferir(self.valor)

        if sucesso_transacao:

            # TODO: transferir de verdade o dinheiro para outra conta

            cartao.conta.historico.adicionar_transacao(self, cartao.conta)
            cartao.historico.adicionar_transacao(self, self.cartao, self.destinatario)
