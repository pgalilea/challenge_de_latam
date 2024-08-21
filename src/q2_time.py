from typing import List, Tuple
from json import loads
from collections import Counter
from itertools import chain

import emoji

def extract_emojis(text):
    return [x.chars for x in emoji.analyze(text)]


def q2_time(file_path: str, top: int = 10) -> List[Tuple[str, int]]:
    """."""

    with open(file_path) as f:
        content = "[" + ",".join(line for line in f) + "]"

    full_json = loads(content)
    emo_list = (tuple(set(extract_emojis(e["content"]))) for e in full_json)
    emo_list_flat = tuple(chain.from_iterable(emo_list))

    return Counter(emo_list_flat).most_common(top)
