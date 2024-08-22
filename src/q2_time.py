from typing import List, Tuple
from json import loads
from collections import Counter
from itertools import chain

from utils import extract_emojis


def q2_time(file_path: str, top: int = 10) -> List[Tuple[str, int]]:
    """
    Obtiene los top n emojis más usados junto a su conteo.

    Transforma el contenido del ndjson en un json válido.
    Lee todo el archivo de una vez.
    Obtiene el conteo de emojis utilizando collections.Counter
    """

    with open(file_path) as f:
        content = "[" + ",".join(line for line in f) + "]"

    full_json = loads(content)
    emo_list = (tuple(set(extract_emojis(e["content"]))) for e in full_json)
    emo_list_flat = tuple(chain.from_iterable(emo_list))  # flatten the iterable

    return Counter(emo_list_flat).most_common(top)
