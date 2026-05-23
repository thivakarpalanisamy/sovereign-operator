from pathlib import Path
from datetime import datetime

ROOT = Path.cwd()

print("\nSOVEREIGN OPERATOR INVENTORY REPORT")
print("-"*40)

for item in ROOT.iterdir():
    item_type = "DIR " if item.is_dir() else "FILE"

    modified = datetime.fromtimestamp(item.stat().st_mtime).strftime("%Y-%m-%d %H:%M:%S")

    size = item.stat().st_size

    print(
        f"{item_type:<5} | "
        f"{item.name:<25} | "
        f"{size:>8} bytes | "
        f"{modified}"
    )