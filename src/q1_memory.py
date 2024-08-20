from typing import List, Tuple
from datetime import datetime

from json import loads


def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    """."""

    result = {}

    with open(file_path) as f:
        for line in f:
            dct_line = loads(line)
            tweet_date = datetime.strptime(dct_line["date"][:10], r'%Y-%m-%d').date()
            # tweet_date = dct_line["date"][:10]
            user = dct_line["user"]["username"]

            if tweet_date in result.keys():
                if user in result[tweet_date].keys():
                    result[tweet_date][user] = result[tweet_date][user] + 1
                else:
                    result[tweet_date][user] = 0
            else:
                result[tweet_date] = {}

    for d in result.keys():
        result[d] = max(result[d], key=result[d].get)
        
    return list(result.items())
