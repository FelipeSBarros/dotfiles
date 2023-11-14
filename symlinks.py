from pathlib import Path

SYMLINKS_FOLDERS = [
    {
        "origin": Path(".config") / "nvim",
        "destination": Path("/home/felipe/.config/nvim"),
    }
]

for folder in SYMLINKS_FOLDERS:
    if not folder.get("origin").exists():
        folder.get("origin").mkdir(parents=True, exist_ok=True)
    if not folder.get("destination").exists():
        folder.get("destination").mkdir(parents=True, exist_ok=False)
    original_files = [folder.get("origin") / "init.vim"]
    for file in original_files:
        dest_file = folder.get("destination") / file.name
        dest_file.absolute().symlink_to(file.absolute())
        dest_file.read_text()
