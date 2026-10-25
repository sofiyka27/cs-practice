import logstats

def main():
    filename = 'events.log'

    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
        if len(lines) == 0:
            print("ВНИМАНИЕ: Файл пуст!")
            return
            
    except FileNotFoundError:
        print(f"ОШИБКА: Файл {filename} не найден в папке! Проверьте расширение.")
        return
    
    counts = logstats.count_levels(lines)
    top_err = logstats.top_errors(lines, 3)
    
    total_lines = sum(counts.values())
    error_lines = counts.get("ERROR", 0)
    broken_lines = counts.get("BROKEN", 0)


    print(total_lines)
    print(error_lines)
    print(broken_lines)


    with open(filename, encoding="utf-8") as log_file:
        top_errs = logstats.top_errors(log_file, 3)     

    report_text = logstats.format_report(counts, top_errs)


    with open("report.txt", "w", encoding="utf-8") as report_file:
        report_file.write(report_text)

if __name__ == "__main__":
    main() 
