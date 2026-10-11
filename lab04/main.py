import sys
from stats import read_valid, average_by_city, warmest_city

def main():
    # Читаем весь ввод
    lines = sys.stdin.read().splitlines()
    
    # Считаем общее количество НЕПУСТЫХ строк (пустые не считаются поданными на вход)
    non_empty_lines = [line for line in lines if line.strip()]
    total_input = len(non_empty_lines)
    
    # Получаем валидные записи
    valid_records = read_valid(lines)
    parsed_count = len(valid_records)
    
    # Пропущенные = все непустые минус валидные
    skipped_count = total_input - parsed_count
    
    averages = average_by_city(valid_records)
    
    if averages:
        best_city = warmest_city(valid_records)
        best_temp = averages[best_city]
    else:
        best_temp = 0.0
        
    # Печатаем ровно 3 строки
    print(parsed_count)
    print(skipped_count)
    print(f"{best_temp:.1f}")

if __name__ == "main":
    main()