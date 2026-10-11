import sys
from stats import read_valid, average_by_city, warmest_city

def main():
    # Читаем весь ввод из стандартного потока
    lines = sys.stdin.read().splitlines()
    
    # 1. Считаем общее количество НЕПУСТЫХ строк (это те, что поданы на вход)
    non_empty_lines = [line for line in lines if line.strip()]
    total_input = len(non_empty_lines)
    
    # 2. Получаем список валидных записей
    valid_records = read_valid(lines)
    parsed_count = len(valid_records)
    
    # 3. Считаем пропущенные: из всех непустых вычитаем валидные
    skipped_count = total_input - parsed_count
    
    # 4. Считаем статистику
    averages = average_by_city(valid_records)
    
    if averages:
        best_city = warmest_city(valid_records)
        best_temp = averages[best_city]
    else:
        # Если валидных записей нет, выводим 0.0
        best_temp = 0.0
        
    # 5. Печатаем ровно 3 строки (как требует задание)
    print(parsed_count)
    print(skipped_count)
    print(f"{best_temp:.1f}")

if __name__ == "main":
    main()