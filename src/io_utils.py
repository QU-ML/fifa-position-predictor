import pathlib
import contextlib
import pandas as pd

from typing import Callable

def write_stdout_to_file(path: pathlib.Path, callback: Callable) -> None:
    with path.open('w') as f:
        with contextlib.redirect_stdout(f):
            callback()
            
def write_df_to_csv(path: pathlib.Path, df: pd.DataFrame) -> None:
    df.to_csv(path, index=False)