from pathlib import Path
from typing import List, Tuple
import logging


def get_directory_path() -> Path:
    while True:
        dir_input = input("\nEnter the main directory path to organize: ").strip()
        directory = Path(dir_input)

        if directory.is_dir():
            return directory
        else:
            print("Invalid directory path")


def collect_all_paths(directory: Path) -> Tuple[List[Path], List[Path]]:
    all_files = []
    all_folders = []

    for item in directory.rglob("*"):
        if item.is_file():
            all_files.append(item)
        elif item.is_dir():
            all_folders.append(item)

    logging.info(f"File count: {len(all_files)} | Folder count : {len(all_folders)}")
    return all_files, all_folders
