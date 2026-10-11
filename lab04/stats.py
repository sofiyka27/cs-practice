def parse_record(line: str) -> dict:
    parts = line.split(';')
    city, temp_str, date = parts
    if len(parts) != 3:
            raise ValueError("полей не ровно 3")
    if not city.strip():
        raise ValueError("значение города пустое")
    if not temp_str.strip():
        raise ValueError("значение температуры пустое")
    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError(f"ntvgthfnehf {temp_str} не является числом")
    return {
        'city': city.strip(),
        'temp': temp,
        'date':date.strip()
            }