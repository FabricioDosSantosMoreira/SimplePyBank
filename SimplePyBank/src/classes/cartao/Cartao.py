from app.Configs import *
from classes.historico.Historico import HistoricoCartao
from datetime import date

import random


# Classe base 'Cartao()' que irá extender outros tipos de cartões
class Cartao():

    def __init__(self, conta) -> None:
        self._conta = conta

        self._historico = HistoricoCartao()
        
        self._titular: str = self.__gerar_titular_cartao(self.conta.cliente.nome)
        self._numero: str = self.__gerar_numero_cartao()
        self._cvv: str = self.__gerar_cvv_cartao()

        self._qtd_digitos_cartao: int 
        self._digito_bandeira: int 
        self._bandeira: str
        self._validade: date
        
        self.carregar_configuracoes()

    @classmethod
    def novo_cartao(cls, conta) -> 'Cartao':
        return cls(conta)

    def carregar_configuracoes(self) -> None:

        self.bandeira = bandeira
        self.digito_bandeira = digito_bandeira
        self.qtd_digitos_cartao = qtd_digitos_cartao

        validade = self.definir_validade(validade_minima)
        self.validade = validade

    def definir_validade(self, validade_em_anos: int) -> None:
        data_atual = date.today()

        # A validade é criada a partir de um date.year + validade_em_anos
        ano = data_atual.year + validade_em_anos
        mes = data_atual.month
        dia = data_atual.day

        return date(year=ano, month=mes, day=dia)

    def __gerar_numero_cartao(self) -> str:

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

    def __gerar_cvv_cartao(self) -> str:

        cvv = ''.join(random.choices('0123456789', k=3))

        return cvv

    def __gerar_titular_cartao(self, nome: str) -> str:
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
    def conta(self):
        return self._conta
    
    @property
    def bandeira(self) -> str:
        return self._bandeira
    
    @bandeira.setter
    def bandeira(self, valor: str) -> None:
        self._bandeira = valor
    
    @property
    def digito_bandeira(self) -> int:
        return self._digito_bandeira
    
    @digito_bandeira.setter
    def digito_bandeira(self, valor: int) -> None:
        self._digito_bandeira = valor
    
    @property
    def qtd_digitos_cartao(self) -> int:
        return self._qtd_digitos_cartao
    
    @qtd_digitos_cartao.setter
    def qtd_digitos_cartao(self, valor: int) -> None:
        self._qtd_digitos_cartao = valor
    
    @property
    def validade(self) -> date:
        return self._validade
    
    @validade.setter
    def validade(self, valor: date) -> None:
        self._validade = valor

    @property
    def titular(self) -> str:
        return self._titular
    
    @property
    def cvv(self) -> str:
        return self._cvv
    
    @property
    def numero(self) -> str:
        return self._numero
    
    @property
    def historico(self) -> 'HistoricoCartao':
        return self._historico
    