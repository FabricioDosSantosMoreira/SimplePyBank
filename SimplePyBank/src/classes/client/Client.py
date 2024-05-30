from datetime import date
from typing import List


# Classe base 'Cliente()' que irá extender outros tipos de clientes
class Client():

    def __init__(self, zip_code: str, name: str, birth_date: date) -> None:
    
        self._accounts: List = [] 

        self._zip_code: str = zip_code
        self._name: str = name
        self._birth_date: date = birth_date

    @classmethod
    def new_client(cls, zip_code: str) -> 'Client':
        return cls(zip_code)
    
    def add_account(self, account) -> None:
        self._accounts.append(account)
    
    def new_transaction(self, transaction, account) -> None:
        from app.Interface import Interface

        today_transactions = account.history.today_transactions()

        if today_transactions >= account.transactions_limit:
            Interface.warn('O número máximo de transacoes diárias já foi atingido. Volte amanhã!', warn_type=0)
            return

        transaction.register(account)

    @property
    def zip_code(self) -> str:
        return self._zip_code
    
    @property
    def accounts(self) -> List:
        return self._accounts

    @property
    def name(self) -> str:
        return self._name

    @property
    def birth_date(self) -> date:
        return self._birth_date