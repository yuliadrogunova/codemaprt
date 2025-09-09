from pathlib import Path
def read_changed_files(path):
    p=Path(path)
    return [l.strip() for l in p.read_text().splitlines() if l.strip()] if p.exists() else []
