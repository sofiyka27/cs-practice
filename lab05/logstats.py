def parce_event(line: str) -> dict:
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
    try:
        event = parse_event(line)
        level = event["level"]
        counts[level] = counts.get(level, 0) + 1
    except ValueError:
        counts["BROKEN"] = counts.get("BROKEN", 0) + 1
        
return counts 

def top_errors(lines, n: int) -> list[list]:
    try:
        event = parse_event(line)
        if event["level"] == "ERROR":
            msg = event["message"]
            errors_count[msg] = errors_count.get(msg, 0) + 1
    except ValueError:
        
        continue
        

    errors_list = [[msg, count] for msg, count in errors_count.items()]


    errors_list.sort(key=lambda x: (-x[1], x[0]))


    return errors_list[:n]
    



    
