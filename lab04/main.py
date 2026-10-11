import sys
from stats import read_valid, average_by_city, warmest_city

def main():
    # Читаем весь ввод
    lines = sys.stdin.read().splitlines()
    
    # 1. Считаем только НЕПУСТЫЕ строки (пустые не считаются ошибками)
    non_empty_lines = [line for line in lines if line.strip()]
    total_input = len(non_empty_lines)
    
    # 2. Получаем валидные записи
    valid_records = read_valid(lines)
    parsed_count = len(valid_records)
    
    # 3. Считаем пропущенные
    skipped_count = total_input - parsed_count
    
    # 4. Считаем статистику
    averages = average_by_city(valid_records)
    
    if averages:
        best_city = warmest_city(valid_records)
        best_temp = averages[best_city]
    else:
        best_temp = 0.0
        
    # 5. Печатаем ровно 3 строки
    print(parsed_count)
    print(skipped_count)
    print(f"{best_temp:.1f}")

if __name__ == "main":
    main()