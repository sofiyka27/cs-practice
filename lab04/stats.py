def parse_record(line: str) -> dict:
    parts = line.split(';')
    city, temp_str, date = parts