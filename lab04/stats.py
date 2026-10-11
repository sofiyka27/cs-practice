def parse_record(line: str) -> dict:
    parts = line.split(';')
    
    # Проверка 1: должно быть ровно 3 части
    if len(parts) != 3:
        raise ValueError("Строка должна содержать ровно 3 поля")
    
    # ОЧИЩАЕМ от пробелов по краям!
    city = parts[0].strip()
    temp_str = parts[1].strip()
    date = parts[2].strip()
    
    # Проверка 2: город не должен быть пустым
    if not city:
        raise ValueError("Название города не может быть пустым")
        
    # Проверка 3: температура должна быть числом
    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError(f"Температура '{temp_str}' не является числом")
        
    return {
        'city': city,
        'temperature': temp, 
        'date': date
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
        temp = rec['temperature'] 
        
        if city not in sums:
            sums[city] = 0.0
            counts[city] = 0
            
        sums[city] += temp
        counts[city] += 1
        
    
    averages = {}
    for city in sums:
        avg = sums[city] / counts[city]
        averages[city] = round(avg, 1)
        
    return averages


def warmest_city(records: list[dict]) -> str:
    
    averages = average_by_city(records)
    
    if not averages:
        return ""
        
    best_city = ""
    max_temp = -float('inf')
   
    for city in sorted(averages.keys()):
        temp = averages[city]
        if temp > max_temp:
            max_temp = temp
            best_city = city
            
    return best_city