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

