from client.Client import Client

from datetime import date


# Extende a classe 'Cliente()'. Herança simples
class StudentClient(Client):

    def __init__(self, zip_code: str, student_card: str, name: str, birth_date: date) -> None:
        super().__init__(zip_code=zip_code, name=name, birth_date=birth_date)

        self._student_card: str = student_card
        
    @property
    def student_card(self) -> str:
        return self._student_card
