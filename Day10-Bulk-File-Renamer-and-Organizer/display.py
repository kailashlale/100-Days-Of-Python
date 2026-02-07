from pathlib import Path
from typing import Dict
import pandas as pd
import logging


def display_folder_structure(
    directory: Path, prefix: str = "", max_depth: int = 3, current_depth: int = 0
):
    if current_depth == 0:
        print(f"\n📁 Folder Structure: {directory.name}/")
        print("=" * 60)

    if current_depth >= max_depth:
        return

    try:
        items = sorted(directory.iterdir(), key=lambda x: (not x.is_dir(), x.name))

        for idx, item in enumerate(items):
            total_items = len(items)
            is_last = idx == total_items - 1

            if is_last:
                current_prefix = "└── "
                extention_prefix = "    "

            else:
                current_prefix = "├── "
                extention_prefix = "│   "

            if item.is_dir():
                print(f"{prefix}{current_prefix}📁 {item.name}/")

                display_folder_structure(
                    item, prefix + extention_prefix, max_depth, current_depth + 1
                )

            else:
                size_kb = item.stat().st_size / 1024
                print(f"{prefix}{current_prefix}📄 {item.name} ({size_kb:.2f} KB)")

    except PermissionError:
        print(f"{prefix}└── ⚠️  [Permission Denied]")


def display_file_summary(df: pd.DataFrame):
    ext_summary = df.groupby("extension").agg({"filename": "count", "size_kb": "sum"})
    ext_summary = ext_summary.rename(
        columns={"filename": "count", "size_kb": "total_size_kb"}
    )
    ext_summary = ext_summary.sort_values("count", ascending=False)

    print("\nFILE SUMMARY")
    print(f"Total Files: {len(df)}")
    print("\nFiles by Extension:")
    print(ext_summary.to_string())


def display_dry_run_preview(move_df: pd.DataFrame, folder_map: Dict[str, Path]):
    print("🔍 DRY-RUN PREVIEW MODE")
    print("\nProposed folder structure after organization:")
    print()

    for ext, _ in sorted(folder_map.items()):
        if ext:
            folder_name = ext.lstrip(".")
        else:
            folder_name = "no_extension"

        files_in_folder = move_df[move_df["extension"] == ext]
        total_size = files_in_folder["size_kb"].sum()

        print(f"📁 {folder_name}/ ({len(files_in_folder)} files, {total_size:.2f} MB)")

        for _, row in files_in_folder.head(5).iterrows():
            print(f"   ├── {row['destination'].name}")

        print()


def get_user_confirmation() -> bool:
    response = input("\nProceed with file organization? (yes/no): ").strip().lower()

    if response in ["yes", "y"]:
        logging.info("User confirmed execution")
        return True
    else:
        logging.info("User cancelled execution")
        return False
