# --------------- scripts/path_utils.py ----------------
from pathlib import Path

# Folder that contains …/Platformer/scripts
_SCRIPT_DIR = Path(__file__).resolve().parent
# Back up one level to …/Platformer
BASE_DIR   = _SCRIPT_DIR.parent
# …/Platformer/assets/images
IMG_DIR    = BASE_DIR / "assets" / "images"
# …/Platformer/assets/sounds
SND_DIR    = BASE_DIR / "assets" / "sounds"
