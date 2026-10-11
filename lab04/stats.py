def parse_record(line: str) -> dict:
    """
    Разбирает строку "город;температура;дата" в словарь.
    Вызывает ValueError, если строка неверная.
    """
    parts = line.split(';')
    
    # Проверка 1: должно быть ровно 3 части
    if len(parts) != 3:
        raise ValueError("Строка должна содержать ровно 3 поля, разделенных ';'")
    
    # Очищаем от пробелов по краям (это лечит тест с пробелами)
    city = parts[0].strip()
    temp_str = parts[1].strip()
    date = parts[2].strip()
    
    # Проверка 2: город не пустой
    if not city:
        raise ValueError("Название города не может быть пустым")
        
    # Проверка 3: температура — число
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
    """
    Принимает список строк, возвращает список только корректных записей.
    Пустые строки и строки с ошибками пропускает молча.
    """
    valid_records = []
    
    for line in lines:
        # Пропускаем пустые строки (и строки из одних пробелов)
        if not line.strip():
            continue
            
        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            # Ловим ошибку парсинга и просто пропускаем эту строку
            pass
            
    return valid_records


def average_by_city(records: list[dict]) -> dict:
    """
    Считает среднюю температуру по каждому городу.
    Округляет до одного знака после запятой.
    """
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
    """
    Находит самый теплый город.
    При равенстве температур выбирает первый по алфавиту.
    """
    averages = average_by_city(records)
    
    if not averages:
        return ""
        
    best_city = ""
    max_temp = -float('inf')
    
    # Сортируем ключи, чтобы при равенстве температур выбрать первый по алфавиту
    for city in sorted(averages.keys()):
        temp = averages[city]
        if temp > max_temp:
            max_temp = temp
            best_city = city
            
    return best_city