from pathlib import Path
from zipfile import ZipFile, BadZipFile
from .config import MAX_ZIP_UNCOMPRESSED

def extract_zip(zip_path: Path, destination: Path) -> Path:
    destination.mkdir(parents=True, exist_ok=True)
    with ZipFile(zip_path) as zf:
        total = 0
        for info in zf.infolist():
            if info.is_dir():
                continue
            total += info.file_size
            if total > MAX_ZIP_UNCOMPRESSED:
                raise ValueError("ZIP محتویات بیش از حد مجاز دارد.")
            target = (destination / info.filename).resolve()
            if not str(target).startswith(str(destination.resolve())):
                raise ValueError("ZIP شامل مسیر غیرمجاز است.")
        zf.extractall(destination)
    return destination
