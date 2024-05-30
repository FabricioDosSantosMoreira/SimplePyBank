from classes.history.History import AccountHistory
from classes.card.Card import Card
from app.Configs import Configs
from typing import Iterator, List
import random


class Account():

    def __init__(self, client, ID: int) -> None:
        self._ID: int = ID

        self._history = AccountHistory()
        self._configs = Configs()
        
        self._cards: List[Card]
        self._client = client

        self._agency: str = self.set_agency(self.configs.agencies)
        self._transactions_count: int = 0
        self._balance: float = 0.0
        

    @classmethod 
    def new_account(cls, client, ID: int) -> 'Account':
        return cls(client, ID)
    

    def set_agency(self, agencies: List[str], index: int = None) -> str:
        if not index:
            index = random.randint(0, len(agencies))

        return agencies[index]


    def add_card(self, card: Card) -> None:
        self.cards.append(card)
    

    def withdraw(self, value: float) -> bool:
        from app.Interface import Interface

        success: bool = False

        if value > self.balance:
            Interface.warn('A operação falhou. Você não possui saldo suficiente', warn_type=2)
        
        elif value <= 0:
            Interface.warn('A operação falhou. O valor informado é inválido!', warn_type=2)

        else:
            self.transactions_count += 1
            self.balance -= value
            Interface.warn(f"Saque de R$ {value:.2f} realizado com sucesso!", warn_type=1)

            success = True

        return success
    

    def deposit(self, value):
        from app.Interface import Interface
        success: bool = False

        if value <= 0:  
            Interface.warn("A operação falhou. O valor informado é inválido!", warn_type=2)
        
        else:
            self.saldo += value
            Interface.warn(f"Depósito de R$ {value:.2f} realizado com sucesso!", warn_type=1)

            self.transactions_count += 1

            success = True

        return success
    

    def transfer(self, value: float) -> bool:
        from app.Interface import Interface

        # TODO: ta mas e se é credito??  nao pode remover o saldo da conta
        success: bool = False

        if value <= 0:
            Interface.warn('A operação falhou. O valor informado é inválido!', warn_type=2)

        elif value> self.saldo:
            Interface.warn("A operação falhou. Você não possui saldo suficiente!", warn_type=2)

        else:
            self.saldo -= value
            Interface.warn(f"Transferência de R$ {value:.2f} é possível!", warn_type=1)

            success = True

        return success


    @property
    def configs(self) -> Configs:
        return self._configs
    
    @property
    def historico(self) -> AccountHistory:
        return self._history
    
    @property
    def cards(self) -> List[Card]:
        return self._cards
    
    @property
    def client(self):
        return self._client

    @property
    def ID(self):
        return self._ID
    
    # Número transações
    @property
    def transactions_count(self) -> int:
        return self._transactions_count

    @transactions_count.setter
    def numero_transacoes(self, value: int) -> None:
        self._transactions_count = value

    # Saldo
    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, value: int) -> None:
        self._balance = value

    # Agência 
    @property
    def agency(self) -> str:
        return self._agency
    
    @agency.setter
    def agency(self, value: str) -> None:
        self._agency = value


class AccountIterator(Iterator):

    __index: int = 0

    def __init__(self, accounts: List[Account]) -> None:
        self._accounts: List[Account] = accounts
    

    def __iter__(self):
        return self


    def __next__(self):
        try:

            account = self.accounts[self.index]

            return f"""Agency: {account.agency}, 
                    ID: {account.ID}, 
                    Holder: {account.client.name}, 
                    Balance: $ {account.balance:.2f}"""

        except IndexError:
            raise StopIteration

        finally:
            self.index += 1

    @property
    def accounts(self) -> List[Account]:
        return self._accounts

    @property
    def index(self) -> int:
        return self.__index
    
    @property
    @index.setter
    def index(self, value) -> None:
        self.__index = value