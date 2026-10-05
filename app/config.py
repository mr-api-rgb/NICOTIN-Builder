from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORKSPACE = ROOT / "workspace"
OUTPUT = ROOT / "output"
MAX_ZIP_UNCOMPRESSED = 2 * 1024 * 1024 * 1024
