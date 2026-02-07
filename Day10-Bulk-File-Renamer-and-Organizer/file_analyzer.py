from pathlib import Path
from typing import List
import pandas as pd
import logging


def collect_file_metadata(files: List[Path]) -> pd.DataFrame:
    file_data = []

    for file in files:
        try:
            stats = file.stat()
            file_info = {
                "original_path": str(file),
                "filename": file.name,
                "extension": file.suffix.lower() if file.suffix else "no_extension",
                "size_kb": round(stats.st_size / 1024, 3),
                "parent_folder": file.parent.name,
            }
            file_data.append(file_info)

        except Exception as e:
            logging.warning(f"Could not read metadata for {file}: {e}")

    df = pd.DataFrame(file_data)

    return df
