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

def read_valid(lines: list[str]) -> list[dict]:
    valid_records = []
    for line in lines:
        if not line.strip():
            continue
        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            pass
    return valid_records

def average_by_city(records: list[dict]) -> dict:
    sums = {}
    counts = {}

    for rec in records:
        city = rec['city']
        temp = ['temp']

        if city not in sums:
            sums[city] = 0.0
            counts[city] = 0
        sums[city] += temp
        counts[city] += 1

    averages = {}
    for city in sums:
        avg = sums[city] / counts[city]
        averages[city] = round(avg,1)
    return averages

def warmest_city(records: list[dict]) ->str:
    averages = average_by_city(records)

    if not averages:
        return ""

    best_city = ""
    max_temp = -float("inf")

    for city in sorted(averages.keys()):
        temp = averages[city]
        if temp > max_temp:
            max_temp = temp
            best_city = city
    return best_city