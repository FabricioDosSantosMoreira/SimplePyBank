from src.app.Interface import Interface

from src.classes.client.Client import Client
from src.classes.card.Card import Card
from src.classes.account.Account import Account


from typing import List


class Main():

    def __init__(self) -> None:
        self.is_running: bool = True
        
        # TODO: DB implementation
        self._clients: List[Client] = []
        self._accounts: List[Account] = []
        self._cards: List[Card] = []
        
        self.interface = Interface(self)

    def run(self) -> None:
        while self.is_running:

            self.interface.menu()

        quit('\nPyBank Closed!')


    def update(self) -> None:
        self.start()
    
    @property
    def clients(self) -> List[Client]:
        return self._clients
    
    @property
    def cards(self) -> List[Card]:
        return self._cards
    
    @property
    def accounts(self) -> List[Account]:
        return self._accounts


if __name__ == '__main__':
    app = Main()
    app.run()
