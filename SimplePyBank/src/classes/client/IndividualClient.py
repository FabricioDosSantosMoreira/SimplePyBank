from client.Client import Client
from datetime import date


# Extende a classe 'Cliente()'. Herança simples
class IndividualClient(Client): 

    def __init__(self, zip_code: str, identification_number: str, name: str, birth_date: date) -> None:
        super().__init__(zip_code=zip_code, name=name, birth_date=birth_date)

        self._identification_number: str = identification_number

    @property
    def identification_number(self) -> str:
        return self._identification_number
    
