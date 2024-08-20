from typing import List, Tuple
from datetime import datetime

import polars as pl


def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    """."""

    df = (
        pl.scan_ndjson(
            file_path,
            schema={
                "url": pl.Utf8,
                "date": pl.Datetime,
                "user": pl.Struct({"username": pl.Utf8}),
            },
        )
        .with_columns(
            user=pl.col("user").struct["username"], date=pl.col("date").dt.date()
        )
        .group_by(["date", "user"])
        .len(name="count")
        .with_columns(pl.col("count").sum().over("date").alias("sum_tweets"))
        .sort(["date", "count"], descending=True)
        .group_by("date")
        .first()
        .select(["date", "user"])
        .sort("date")
    )

    # print(df.collect().head(20))
    # print(df.collect().head(20).rows())

    return df.collect().rows()
