import os


def count_by_extension(paths: list[str]) -> dict[str, int]:
    counts = {}
    for path in paths:
        ext = os.path.splitext(path)[1]
        if ext.startswith('.'):
            ext = ext[1:].lower()
        
        counts[ext] = counts.get(ext, 0) + 1
    return counts


def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""
    
    return max(paths, key=lambda p: (p.count('/'), [-ord(c) for c in p]))

def human_size(n_bytes: int) -> str:
    if n_bytes < 1024:
        return f"{n_bytes} Б"
    
    units = ["КБ", "МБ", "ГБ", "ТБ"]
    size = n_bytes / 1024.0
    
    unit_index = 0
    while size >= 1024 and unit_index < len(units) - 1:
        size /= 1024.0
        unit_index += 1
        
    return f"{round(size, 1)} {units[unit_index]}"