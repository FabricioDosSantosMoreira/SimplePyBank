from app.Interface import Interface
from typing import Union


def ler_str(*, msg: str) -> Union[str, int]:
    while True:

        try:
            valor_str = str(input(msg))

            if not valor_str or valor_str.isspace():
                raise ValueError

            return valor_str

        except ValueError:
            Interface.avisar('Entrada inválida. Por favor, tente novamente.', tipo_aviso=2)

        except KeyboardInterrupt:
            Interface.avisar('Programa interrompido pelo usuário.', tipo_aviso=2)
            return -1
        
        except Exception as e:
            Interface.avisar(f'Ocorreu um erro: {e}', tipo_aviso=2)
            return -1


def ler_int(*, msg: str) -> Union[str, int]:
    while True:

        try:
            valor_int: int = int(input(msg))
            return valor_int

        except ValueError:
            Interface.avisar('Entrada inválida. Por favor, tente novamente.', tipo_aviso=2)

        except KeyboardInterrupt:
            Interface.avisar('Programa interrompido pelo usuário.', tipo_aviso=2)
            return -1
        
        except Exception as e:
            Interface.avisar(f'Ocorreu um erro: {e}', tipo_aviso=2)
            return -1
        