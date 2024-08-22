from typing import List, Tuple
from json import loads


def q3_memory(file_path: str, top: int = 10) -> List[Tuple[str, int]]:
    """
    Obtiene los top n usuarios más influyentes en función de las menciones

    Lee el archivo línea por línea.
    Utiliza un diccionario para hacer el conteo.
    """

    result = {}  # keys son el nombre de usuario, values son el conteo

    with open(file_path) as f:
        for line in f:
            dct_line = loads(line)
            ment_users = dct_line["mentionedUsers"]  # list of dicts (mentioned users)
            if ment_users is not None:
                for usr in ment_users:
                    if usr["username"] in result.keys():
                        result[usr["username"]] = result[usr["username"]] + 1
                    else:
                        result[usr["username"]] = 1

    result = sorted(list(result.items()), key=lambda tup: tup[1], reverse=True)

    return result[:top]
