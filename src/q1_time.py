from typing import List, Tuple
from datetime import datetime

import polars as pl


def q1_time(file_path: str, top: int = 10) -> List[Tuple[datetime.date, str]]:
    """
    Obtiene las top n fechas donde hay más tweets junto al usuario con más tweets en cada fecha.

    Utiliza polars para leer el ndjson de forma Lazy.
    Utiliza agrupaciones y agregaciones para procesar los datos.
    Se transforma el dataframe a una lista de tuplas.
    """

    df = (
        pl.scan_ndjson(
            file_path,
            schema={
                # "url": pl.Utf8,
                "date": pl.Datetime,
                "user": pl.Struct({"username": pl.Utf8}),
            },
        )
        .with_columns(
            user=pl.col("user").struct["username"], date=pl.col("date").dt.date()
        )
        .group_by(["date", "user"])
        .len(name="user_count")
        .with_columns(day_tweets=pl.col("user_count").sum().over("date"))
        .group_by("date")
        .agg(
            pl.col("user").sort_by("user_count", descending=True).first(),
            pl.col("day_tweets").max(),
        )
        .sort("day_tweets", descending=True)
        .select(["date", "user"])
    )

    # print(df.head(10).collect())
    # print(df.head(20).collect().rows())

    return df.head(top).collect().rows()
