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


    


    
