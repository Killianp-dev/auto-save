import pytest
from pathlib import Path
import shutil
from utils import auto_save

@pytest.fixture
def temp_dirs(tmp_path):
    """Crée des répertoires temporaires pour les tests."""
    source_dir = tmp_path / "source"
    dest_dir = tmp_path / "dest"
    source_dir.mkdir()
    dest_dir.mkdir()

    # Ajouter des fichiers dans le répertoire source
    for i in range(3):
        (source_dir / f"file_{i}.txt").write_text(f"Contenu du fichier {i}")

    return source_dir, dest_dir

def test_auto_save(temp_dirs):
    """Teste la fonction auto_save."""
    source_dir, dest_dir = temp_dirs

    # Appeler la fonction auto_save
    auto_save(str(source_dir), str(dest_dir))

    # Vérifier si un nouveau dossier a été créé dans dest_dir
    backup_dirs = list(dest_dir.iterdir())
    assert len(backup_dirs) == 1, "Le dossier de sauvegarde n'a pas été créé."

    # Vérifier si les fichiers ont été copiés correctement
    backup_dir = backup_dirs[0]
    for i in range(3):
        file_path = backup_dir / f"file_{i}.txt"
        assert file_path.exists(), f"Le fichier {file_path} n'a pas été copié."

    # Vérifier le contenu des fichiers
    for i in range(3):
        file_path = backup_dir / f"file_{i}.txt"
        assert file_path.read_text() == f"Contenu du fichier {i}"


