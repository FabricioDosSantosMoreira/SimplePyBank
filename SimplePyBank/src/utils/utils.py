from typing import Any


def categorizar_lista(lista: list[Any], identificadores: list[Any] = []) -> list[list[Any]]:
    lista_categorizada: list[list[Any]] = []

    if not identificadores: 
        identificadores = []

        for n in range(len(lista)):
            # Atribui identificadores baseado no indíce da lista + 1.
            identificadores.append(str(n + 1))  

    for i in range(len(lista)): 
        # Cria uma sublista contendo identificadores e os elementos da lista.
        lista_categorizada.append([identificadores[i], lista[i]]) 

    return lista_categorizada


def garantir_paridade(valor: int, *, paridade_alvo: str = None, diminuir: bool = False) -> int:

    if paridade_alvo not in ["par", "ímpar"]:
        raise ValueError("\n\n\nValueError - - -> 'paridade_alvo' Deve ser 'par' ou 'ímpar'.\n")

    paridade_atual = "par" if valor % 2 == 0 else "ímpar"

    if paridade_atual != paridade_alvo:
        if diminuir:
            return valor - 1
        else:
            return valor + 1

    return valor  # valor já possui a paridade alvo.




def atribuir_valores_distribuidos(size: int, value: int, assign_value_at_end: bool = False) -> list[int]:
    """
    Assigns integers representing lengths to a list, distributing a given value evenly across the list or at the end.

    Args:
        size (int): The size of the list.
        value (int): The value to be distributed across the list.
        assign_value_at_end (bool): Indicates whether the value should be placed at the last index of the list.

    Returns:
        list[int]: A list of integers with assigned lengths.
    """

    # If 'value' is to be placed at the last index
    if assign_value_at_end:
        size_list = [0] * size  # Initialize list with zeros
        size_list[-1] = value  # Assign the value to the last index

    # If 'value' is to be distributed evenly across the list
    else:
        distributed_value = value // size  # Calculate the value to be distributed
        size_list = [distributed_value] * size  # Initialize list with distributed values

    return size_list  # Return the list with assigned lengths