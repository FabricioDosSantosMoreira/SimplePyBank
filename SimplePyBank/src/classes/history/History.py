import pytz

from classes.transaction.Transaction import Transaction

from datetime import datetime
from typing import List


class History():

    def __init__(self) -> None:
        self._transactions: List[Transaction]

    def relatory(self, transaction_type = None):

        for transaction in self.transactions:
            if (transaction_type is None or transaction['Type'].lower() == transaction_type.lower()):
                
                yield transaction

    @property
    def transactions(self) -> List:
        return self._transactions


# O histórico de um determinado cartão
class CardHistory(History):

    def __init__(self) -> None:
        super().__init__()

    def add_transaction(self, transaction: Transaction, card, identifier: str = None) -> None:
        # O identificador teóricamente seria um cpf, cnpj ou matricula estudante

        receiver = "you" if identifier is None else identifier

        self._transactions.append(
            {
                "Type": transaction.__class__.__name__,
                "Value": transaction.value,
                "Date": datetime.now(pytz.timezone("UTC")),
                "Card": card.number,
                "To": receiver
            }
        )


# O histórico da conta e todos os cartoes
class AccountHistory(History):
    
    def __init__(self) -> None:
        super().__init__()

    def add_transaction(self, transaction: Transaction, account) -> None:
        self._transactions.append(
            {
                "Type": transaction.__class__.__name__,
                "Value": transaction.value,
                "Date": datetime.now(pytz.timezone("UTC")),
                "Card": account.cliente
            }
        )


    def transactions_of_the_day(self) -> int:
        current_day = datetime.now(pytz.timezone("UTC")).day
        transactions_count: int = 0

        for transaction in self.transactions:

            transaction_day = transaction["Date"].day

            if transaction_day == current_day:
                transactions_count += 1

        return transactions_count
