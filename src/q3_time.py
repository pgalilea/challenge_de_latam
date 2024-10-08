from typing import List, Tuple

import polars as pl

def q3_time(file_path: str, top: int = 10) -> List[Tuple[str, int]]:
    """
    Obtiene los top n usuarios más influyentes en función de las menciones
    
    Utiliza polars para leer el ndjson de forma Lazy.
    Utiliza una agrupación y transformaciones para procesar los datos.
    Se transforma el dataframe a una lista de tuplas.
    """

    df = (
        pl.scan_ndjson(
            file_path,
            schema={
                "date": pl.Datetime,
                "mentionedUsers": pl.List(pl.Struct({"username": pl.Utf8})),
            },
        )
        .filter(pl.col("mentionedUsers").is_not_null())
        .with_columns(date=pl.col("date").dt.date())
        .explode("mentionedUsers")
        .with_columns(mentioned_user=pl.col("mentionedUsers").struct["username"])
        .select(["date", "mentioned_user"])
        .group_by(["mentioned_user"])
        .len(name="count")
        .sort("count", descending=True)
    )

    return df.head(top).collect().rows()