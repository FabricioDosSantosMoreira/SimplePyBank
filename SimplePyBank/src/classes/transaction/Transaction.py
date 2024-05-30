from abc import ABC, abstractmethod


# Classe abstrata que herda as funcionalidades do módulo ABC (Abstract Base Classes)
class Transaction(ABC):

    _value: float 

    @property
    @abstractmethod
    def value(self) -> float:
        return self._value

    @value.setter
    def value(self, value: float) -> None:
        self._value = value

    @abstractmethod
    def register(self, account) -> None:
        pass


# Extende a classe 'Transacao()'. Herança simples
class Deposit(Transaction):

    def __init__(self, value: float) -> None:
        self._value = value

    def register(self, account) -> None:

        success: bool = account.deposit(self.value)

        if success:
            account.history.add_transaction(self, account)
            

# Extende a classe 'Transacao()'. Herança simples
class Withdraw(Transaction):

    def __init__(self, value: float) -> None:
        self._value = value

    def register(self, account) -> None:

        success: bool = account.withdraw(self.value)

        if success:
            account.history.add_transaction(self, account)


# Extende a classe 'Transacao()'. Herança simples
class Transfer(Transaction):

    def __init__(self, value: float, receiver: str) -> None:
        self._value = value
        self.receiver = receiver

    def register(self, card) -> None:
        
        success: bool = card.account.transfer(self.value)

        if success:
            # TODO: transferir de verdade o dinheiro para outra conta

            card.account.history.add_transaction(self, card.account)
            card.history.add_transaction(self, card, self.receiver)
