from pathlib import Path
import logging
from datetime import datetime


def setup_logging(log_dir: Path) -> Path:
    log_dir.mkdir(exist_ok=True)
    log_file = (
        log_dir / f"file_organizer_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    )

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[logging.FileHandler(log_file), logging.StreamHandler()],
    )

    logging.info("=" * 50)
    logging.info("File Organizer Started")
    logging.info("=" * 50)

    return log_file
