def parse_record(line: str) -> dict:
    """
    Разбирает одну строку журнала в словарь.
    Если строка неверная, вызывает ValueError.
    """
    # Разбиваем строку строго по точке с запятой
    parts = line.split(';')
    
    # Проверка 1: должно быть ровно 3 части
    if len(parts) != 3:
        raise ValueError("Строка должна содержать ровно 3 поля, разделенных ';'")
    
    city, temp_str, date = parts
    
    # Проверка 2: город не должен быть пустым
    if not city.strip():
        raise ValueError("Название города не может быть пустым")
        
    # Проверка 3: температура должна быть числом
    try:
        temp = float(temp_str)
    except ValueError:
        # Если float() не смог преобразовать, вызываем свою ошибку
        raise ValueError(f"Температура '{temp_str}' не является числом")
        
    # ВАЖНО: Возвращаем словарь с ключом 'temperature', как ожидает система!
    return {
        'city': city.strip(),
        'temperature': temp, 
        'date': date.strip()
    }


def read_valid(lines: list[str]) -> list[dict]:
    """
    Принимает список строк, возвращает список только корректных записей (словарей).
    Пустые строки и строки с ошибками пропускает.
    """
    valid_records = []
    
    for line in lines:
        # Пропускаем пустые строки молча (не считаем их ошибками)
        if not line.strip():
            continue
            
        try:
            # Пытаемся разобрать строку
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            # Если parse_record вызвал ошибку, просто пропускаем эту строку
            pass
            
    return valid_records


def average_by_city(records: list[dict]) -> dict:
    """
    Считает среднюю температуру для каждого города.
    Возвращает словарь вида {'Город': средняя_температура}.
    """
    sums = {}
    counts = {}
    
    # Собираем сумму температур и количество записей для каждого города
    for rec in records:
        city = rec['city']
        # ИСПОЛЬЗУЕМ КЛЮЧ 'temperature' вместо 'temp'!
        temp = rec['temperature'] 
        
        if city not in sums:
            sums[city] = 0.0
            counts[city] = 0
            
        sums[city] += temp
        counts[city] += 1
        
    # Вычисляем среднее и округляем до одного знака после запятой
    averages = {}
    for city in sums:
        avg = sums[city] / counts[city]
        averages[city] = round(avg, 1)
        
    return averages


def warmest_city(records: list[dict]) -> str:
    """
    Находит самый теплый город на основе средних температур.
    При равенстве температур выбирает первый по алфавиту.
    """
    averages = average_by_city(records)
    
    if not averages:
        return ""
        
    best_city = ""
    max_temp = -float('inf')
    
    # Ищем город с максимальной температурой
    # Сортируем ключи (названия городов), чтобы при равенстве температур
    # выбрать первый по алфавиту
    for city in sorted(averages.keys()):
        temp = averages[city]
        if temp > max_temp:
            max_temp = temp
            best_city = city
            
    return best_city