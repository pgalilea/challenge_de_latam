from typing import List, Tuple
from json import loads

from utils import extract_emojis


def q2_memory(file_path: str, top: int = 10) -> List[Tuple[str, int]]:
    """
    Obtiene los top n emojis más usados junto a su conteo.
    
    Lee línea por línea el archivo.
    Extrae los emojis utilizando una biblioteca externa.
    Guarda en un diccionario el conteo de cada emoji.
    """

    result = {}  # emojis como keys y conteo como values

    with open(file_path) as f:
        for line in f:
            dct_line = loads(line)
            emojis = set(
                extract_emojis(dct_line["content"])
            )  # mismo emoji varias veces en un tweet, se considera solo uno

            for e in emojis:
                if e in result.keys():
                    result[e] = result[e] + 1
                else:
                    result[e] = 1

    result = sorted(list(result.items()), key=lambda tup: tup[1], reverse=True)

    return result[:top]
