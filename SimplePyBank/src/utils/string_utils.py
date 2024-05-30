from typing import List

def reduzir_string(string: str, *, tamanho: int = 30, delimitador: str = "", cortar_final: bool = True) -> str:

    if tamanho <= 0:
        raise ValueError(f"\n\n\nValueError - - -> 'tamanho' Deve ser um inteiro positivo. Recebeu: {tamanho}\n")

    if tamanho >= len(string):  # O tamanho é maior ou igual a string? Então retorna a string
        return string

    if cortar_final:  # cortar_final é True? Então retorna a string com o corte no final + delimitador
        return string[0:tamanho] + delimitador
    
    else:
        # Retorna a string com o delimitador + corte no início
        return delimitador + string[len(string) - tamanho:len(string)]


def reduzir_lista_de_strings(lista_de_strings: List[str], *, tamanho: int = 30, delimitador: str = "", cortar_final: bool = True) -> list[str]:
    
    for i, string in enumerate(lista_de_strings):
        lista_de_strings[i] = reduzir_string(string, tamanho=tamanho, delimitador=delimitador, cortar_final= cortar_final,)

    return lista_de_strings


def contem_ascii(string: str) -> bool:
    for char in string:

        if ord(char) > 127:
            return False
        
    return True