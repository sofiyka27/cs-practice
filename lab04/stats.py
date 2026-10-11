def parse_record(line: str) -> dict:
    parts = line.split(';')
    city, temp_str, date = parts
    if len(parts) != 3:
            raise ValueError("полей не ровно 3")