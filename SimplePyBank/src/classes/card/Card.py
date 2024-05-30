from app.Configs import Configs
from classes.history.History import CardHistory
from datetime import date

import random


# Classe base 'Cartao()' que irá extender outros tipos de cartões
class Card():

    def __init__(self, account) -> None:
        self._account = account
        self._history = CardHistory()
        self._configs = Configs()

        self._card_holder: str = self.__generate__card_holder(self.account.client.name)
        self._card_number: str = self.__generate_card_number()
        self._cvv: str = self.__generate_cvv()

        self._card_digit_count: int = self.configs.card_digit_count
        self._flag_digit: int = self.configs.flag_digit
        self._flag: str = self.configs.flag
        self._validity: date = self.set_validity(self.configs.minimum_validity)
        
    
    @classmethod
    def new_card(cls, account) -> 'Card':
        return cls(account)


    def set_validity(self, validade_em_anos: int) -> date:
        data_atual = date.today()

        # A validade é criada a partir de um date.year + validade_em_anos
        ano = data_atual.year + validade_em_anos
        mes = data_atual.month
        dia = data_atual.day

        return date(year=ano, month=mes, day=dia)


    def __generate_card_number(self) -> str:

        # O primeiro digito do cartão
        digito_inicial = str(self.digito_bandeira)

        # Digitos aletórios
        digitos_meio = ''.join(random.choices('0123456789', k=self.qtd_digitos_cartao))

        # Calcula o o último dígito usando o algoritmo de Luhn
        soma = sum(int(digito) for digito in digito_inicial + digitos_meio)
        soma *= 9

        if soma % 10 == 0:
            ultimo_digito = 0

        else:
            ultimo_digito = soma % 10

        # Concatena todos os dígitos para formar o número do cartão completo
        numero_cartao = digito_inicial + digitos_meio + str(ultimo_digito)

        return numero_cartao

    def __generate_cvv(self) -> str:

        cvv = ''.join(random.choices('0123456789', k=3))

        return cvv

    def __generate__card_holder(self, nome: str) -> str:
        titular: str = ""

        # Separa o nome e os sobrenomes
        substrings_nome = nome.split(' ') 

        # Adiciona o nome
        titular += f"{substrings_nome[0]}"

        # percorre do primeiro índice até o penúltimo índice
        for i in range(1, len(substrings_nome) - 1):

            # Adiciona os sobrenomes abreviados
            titular += f" {substrings_nome[i][0] + '.'}"

        # Adiciona o último sobrenome
        titular += f" {substrings_nome[-1]}"

        return titular.title()

    # TODO: Implementar o algoritmo de Luhn
    def verificar_algoritmo_luhn() -> bool:
        pass

    # TODO: Implementar o método __str__

    @property
    def configs(self) -> Configs:
        return self._configs

    @property
    def account(self):
        return self._account
    
    @property
    def flag(self) -> str:
        return self._flag
    
    @flag.setter
    def flag(self, value: str) -> None:
        self._flag = value
    
    @property
    def flag_digit(self) -> int:
        return self._flag_digit
    
    @flag_digit.setter
    def flag_digit(self, value: int) -> None:
        self._flag_digit = value
    
    @property
    def card_digit_count(self) -> int:
        return self._card_digit_count
    
    @card_digit_count.setter
    def card_digit_count(self, value: int) -> None:
        self._card_digit_count = value
    
    @property
    def validity(self) -> date:
        return self._validity
    
    @validity.setter
    def validity(self, value: date) -> None:
        self._validity = value

    @property
    def card_holder(self) -> str:
        return self._card_holder
    
    @property
    def cvv(self) -> str:
        return self._cvv
    
    @property
    def card_number(self) -> str:
        return self._card_number
    
    @property
    def history(self) -> 'CardHistory':
        return self._history
    