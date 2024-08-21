from typing import List, Tuple
from datetime import datetime

from json import loads



def q1_memory(file_path: str, top: int = 10) -> List[Tuple[datetime.date, str]]:
    """."""

    result = {}

    with open(file_path) as f:
        for line in f:
            dct_line = loads(line)
            tweet_date = datetime.strptime(dct_line["date"][:10], r"%Y-%m-%d").date()
            # tweet_date = dct_line["date"][:10]
            user = dct_line["user"]["username"]

            if tweet_date in result.keys():
                if user in result[tweet_date].keys():
                    result[tweet_date][user] = result[tweet_date][user] + 1
                else:
                    result[tweet_date][user] = 1
            else:
                result[tweet_date] = {user: 1}

    for d in result.keys():
        result[d] = (sum(result[d].values()), max(result[d], key=result[d].get))

    result = sorted(list(result.items()), key=lambda tup: tup[1][0], reverse=True)[:top]

    # for _d, (_c, _u) in result:
    #     print(_d, _c, _u)

    return [(_date, _user) for _date, (_count, _user) in result]


