import sys
from stats import read_valid, average_by_city, warmest_city

def main():
    # Читаем весь ввод из стандартного потока (stdin)
    lines = sys.stdin.read().splitlines()
    
    # 1. Считаем общее количество непустых строк
    # Внимание: система может считать "пропущенными" только те строки, 
    # которые не являются пустыми, но не прошли валидацию.
    # Обычно: total = len([l for l in lines if l.strip()])
    total_lines = len([line for line in lines if line.strip()])
    
    # 2. Получаем список валидных (правильных) записей
    valid_records = read_valid(lines)
    
    # 3. Считаем, сколько записей успешно разобрано
    parsed_count = len(valid_records)
    
    # 4. Считаем, сколько строк пропущено
    skipped_count = total_lines - parsed_count
    
    # 5. Вычисляем средние температуры и находим самый теплый город
    averages = average_by_city(valid_records)
    
    # Если есть валидные записи, находим лучший город и его температуру
    if averages:
        best_city = warmest_city(valid_records)
        best_temp = averages[best_city]
    else:
        best_temp = 0.0
        
    # 6. Печатаем результат в нужном порядке
    print(parsed_count)
    print(skipped_count)
    # Форматируем вывод, чтобы было ровно 1 знак после запятой
    print(f"{best_temp:.1f}")

if __name__ == "main":
    main()