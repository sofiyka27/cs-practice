def parse_event(line: str) -> dict:
    line = line.strip() 
    if not line: 
        raise ValueError("Пустая строка")
    parts = line.split(maxsplit=2)


    if len(parts) != 3:
        raise ValueError("Неверный формат строки")

    time, level, message = parts

    valid_levels = {"DEBUG", "INFO", "WARNING", "ERROR"}
    if level not in valid_levels:
        raise ValueError("Неизвестный уровень логирования")

    return {
        "time": time,
        "level": level,
        "message": message
    }

def count_levels(lines) -> dict:
    counts = {}
    for line in lines: 
        if not line.strip(): 
            continue
    try:
        event = parse_event(line)
        level = event["level"]
        counts[level] = counts.get(level, 0) + 1
    except ValueError:
        counts["BROKEN"] = counts.get("BROKEN", 0) + 1
    return counts 


def top_errors(lines, n: int) -> list[dict]: 
    errors_count = {} 
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
            if event["level"] == "ERROR":
                msg = event["message"]
                errors_count[msg] = errors_count.get(msg, 0) + 1
        except ValueError:
            continue
            
    errors_list = [(msg, count) for msg, count in errors_count.items()]
    
    def sort_key(item):
        msg, count = item
        return -count, msg
        
    errors_list.sort(key=sort_key)

    result = []
    
    for msg, count in errors_list[:n]:
        result.append({'message': msg,"count": count})
    
    return result


def format_report(counts: dict, errors: list[list]) -> str: 
    report = "Отчёт по журналу\n\n"

    for level in sorted(counts.keys()):
        report += f"{level}: {counts[level]}\n"
    
    report += "\nЧастые ошибки:\n"


    for msg, count in errors:
        report += f"- {msg} — {count}\n"
    
    return report

    
