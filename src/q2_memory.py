from typing import List, Tuple
from json import loads

import emoji


def extract_emojis(text):
    return [x.chars for x in emoji.analyze(text)]


def q2_memory(file_path: str, top: int = 10) -> List[Tuple[str, int]]:
    """."""

    result = {}

    with open(file_path) as f:
        for line in f:
            dct_line = loads(line)
            emojis = set(extract_emojis(dct_line["content"])) # mismo emoji varias veces en un tweet, se considera solo uno

            for e in emojis:
                if e in result.keys():
                    result[e] = result[e] + 1
                else:
                    result[e] = 1

    result = sorted(list(result.items()), key=lambda tup: tup[1], reverse=True)

    return result[:top]
