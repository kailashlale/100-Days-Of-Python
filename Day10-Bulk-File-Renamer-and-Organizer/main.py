import logging

# Import from our modules
from logger_config import setup_logging
from file_scanner import get_directory_path, collect_all_paths
from file_analyzer import collect_file_metadata
from organizer import (
    handle_filename_conflicts,
    create_organization_plan,
    create_move_plan,
    execute_file_organization,
)
from display import (
    display_folder_structure,
    display_file_summary,
    display_dry_run_preview,
    get_user_confirmation,
)


def main():
    print()
    print("   FILE ORGANIZER - Organize Files by Extension")

    main_directory = get_directory_path()

    log_file = setup_logging(main_directory / "_logs")
    logging.info(f"Selected Directory: {main_directory.absolute()}")

    organized_dir = main_directory.parent / f"{main_directory.name}_organized"
    organized_dir.mkdir(exist_ok=True)

    print("\nScanning directory...")
    all_files, _ = collect_all_paths(main_directory)

    if not all_files:
        print("\nNo files found in the directory.")
        logging.warning("No files found to organize")
        return

    display_folder_structure(main_directory)

    print("\n Analyzing files...")
    file_df = collect_file_metadata(all_files)
    display_file_summary(file_df)

    show_preview = input("\nShow dry-run preview? (yes/no): ").strip().lower()
    if show_preview in ["yes", "y"]:
        file_df = handle_filename_conflicts(file_df, organized_dir)
        folder_map = create_organization_plan(file_df, organized_dir)
        move_df = create_move_plan(file_df, folder_map)
        display_dry_run_preview(move_df, folder_map)

    print(f"\n📁 Organized files will be saved to: {organized_dir}")

    if not get_user_confirmation():
        print("\nOperation cancelled by user.")
        return

    execute_file_organization(move_df, folder_map)

    print("\nFinal Folder Structure:")
    display_folder_structure(organized_dir, max_depth=2)

    print(f"\nLog file saved: {log_file}")
    print("\nFile organization completed successfully!")


if __name__ == "__main__":
    main()
