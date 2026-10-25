from collections import Counter


def parse_event(line: str) -> dict:
    parts = line.split(maxsplit=2)
    if len(parts) < 3:
        raise ValueError("Неверный формат строки")
    
    time_and_date, level, message = parts
    
    allowed_levels = {"DEBUG", "INFO", "WARNING", "ERROR"}
    if level not in allowed_levels:
        raise ValueError("Неизвестный уровень")
    
    return {
        "time": time_and_date,
        "level": level,
        "message": message.strip()
    }


def count_levels(lines) -> dict:
    counts = {}
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            event = parse_event(line)
            level = event["level"]
            counts[level] = counts.get(level, 0) + 1
        except ValueError:
            counts["BROKEN"] = counts.get("BROKEN", 0) + 1
            
    return counts


def top_errors(lines, n: int) -> list:
    error_messages = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            event = parse_event(line)
            if event["level"] == "ERROR":
                error_messages.append(event["message"])
        except ValueError:
            pass
            
    counter = Counter(error_messages)
    
    sorted_errors = sorted(counter.items(), key=lambda item: (-item[1], item[0]))
    
    return sorted_errors[:n]


def format_report(counts: dict, errors: list) -> str:
    report_lines = ["Отчёт по журналу", ""]
    
    for level in sorted(counts.keys()):
        report_lines.append(f"{level}: {counts[level]}")
        
    report_lines.append("")
    report_lines.append("Частые ошибки:")
    
    for message, count in errors:
        report_lines.append(f"- {message} — {count}")
        
    return "\n".join(report_lines) + "\n"