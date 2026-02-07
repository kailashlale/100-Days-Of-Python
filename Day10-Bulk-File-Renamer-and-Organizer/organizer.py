from pathlib import Path
import pandas as pd
from collections import defaultdict
from typing import Dict
import logging
import shutil


def handle_filename_conflicts(df: pd.DataFrame, target_dir: Path) -> pd.DataFrame:
    filename_counter = defaultdict(int)
    new_filenames = []

    for _, row in df.iterrows():
        extension = row["extension"]
        original_name = row["filename"]
        stem = Path(original_name).stem

        target_subfolder = target_dir / extension.lstrip(".")
        target_path = target_subfolder / original_name

        if target_path.exists() or filename_counter[original_name] > 0:
            filename_counter[original_name] += 1
            new_name = f"{stem}_{filename_counter[original_name]}{extension}"
            logging.info(f"Conflict detected: {original_name} → {new_name}")
        else:
            new_name = original_name
            filename_counter[original_name] += 1

        new_filenames.append(new_name)

    df["new_filename"] = new_filenames
    return df


def create_organization_plan(df: pd.DataFrame, target_dir: Path) -> Dict[str, Path]:
    unique_extensions = sorted(df["extension"].unique())
    folder_map = {}

    print("\n📂 FOLDERS TO BE CREATED")

    for ext in unique_extensions:
        if ext:
            folder_name = ext.lstrip(".")
        else:
            folder_name = "no_extension"

        folder_path = target_dir / folder_name
        folder_map[ext] = folder_path
        file_count = len(df[df["extension"] == ext])
        print(f"  • {folder_name}/ ({file_count} files)")

    logging.info(f"Created organization plan for {len(folder_map)} extensions")
    return folder_map


def create_move_plan(df: pd.DataFrame, folder_map: Dict[str, Path]) -> pd.DataFrame:
    move_operations = []

    for _, row in df.iterrows():
        operation = {
            "source": Path(row["original_path"]),
            "destination": folder_map[row["extension"]] / row["new_filename"],
            "extension": row["extension"],
            "size_kb": row["size_kb"],
        }
        move_operations.append(operation)

    move_df = pd.DataFrame(move_operations)
    logging.info(f"Created move plan for {len(move_df)} files")

    return move_df


def execute_file_organization(move_df: pd.DataFrame, folder_map: Dict[str, Path]):
    print("🚀 EXECUTING FILE ORGANIZATION")
    print("=" * 60)

    for folder_path in folder_map.values():
        folder_path.mkdir(parents=True, exist_ok=True)
        logging.info(f"Created folder: {folder_path}")

    success_count = 0
    error_count = 0

    for _, row in move_df.iterrows():
        try:
            source = row["source"]
            destination = row["destination"]

            destination.parent.mkdir(parents=True, exist_ok=True)

            shutil.copy(str(source), str(destination))

            success_count += 1
            logging.info(f"✓ Moved: {source.name} → {destination}")
            print(f"✓ [{success_count}/{len(move_df)}] {source.name}")

        except Exception as e:
            error_count += 1
            logging.error(f"✗ Failed to move {source.name}: {e}")
            print(f"✗ Error moving {source.name}")
