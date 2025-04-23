from pathlib import Path
import shutil
from datetime import datetime
from loguru import logger

BASE_DIR = Path(__file__).resolve().parent

# Configuration de Loguru
LOG_FILE = BASE_DIR / 'auto_save.log'
logger.remove()  # delete default handlers
logger.add(LOG_FILE, rotation="2 KB", retention=3, format="{time} - {level} - {message}")

"""
Modèles de message :
logger.debug('message')
logger.info('message')
logger.warning('message')
logger.error('message')
logger.critical('message')
"""

def auto_save(source_path: str, dest_dir_path: str) -> None:
    """Automatically save a directory.
    
    Creates a new backup directory in the specified directory path.

    Args:
        source_path (str): The source directory path to be backed up.
        dest_dir_path (str): The destination directory path where the backup will be stored.
    """
    source = Path(source_path).resolve()
    date = datetime.now()
    format_date = date.strftime("%d_%m_%Y %Hh_%Mm_%Ss")
    destination = Path(dest_dir_path).resolve() / f"Documents {format_date}"

    try:
        shutil.copytree(source, destination, symlinks=True)
        logger.info(f"[ADD] {destination.name}")
    except Exception as e:
        logger.error(f"Error during auto_save: {e}")

def supprimer_ancien_dossier(dest_dir_path: str) -> None:
    """Delete old directories.
    
    Searches for and deletes old directories in the specified directory path.

    Args:
        dest_dir_path (str): The directory path where we need to find old directories to delete.
    """
    d = Path(dest_dir_path).resolve()
    try:
        dossier_source = sorted(d.iterdir(), key=lambda x: x.stat().st_ctime)

        if len(dossier_source) > 1:
            dossier_a_supprimer = dossier_source[0]
            shutil.rmtree(dossier_a_supprimer)
            logger.info(f"[DELETE] {dossier_a_supprimer.name}")
    except Exception as e:
        logger.error(f"Error during supprimer_ancien_dossier: {e}")
