from logstats import parse_event, count_levels, top_errors, format_report


def main():
    filename = input().strip()
    
    total_lines = 0
    error_lines = 0
    broken_lines = 0
    
    try:
        with open(filename, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                total_lines += 1
                try:
                    event = parse_event(line)
                    if event["level"] == "ERROR":
                        error_lines += 1
                except ValueError:
                    broken_lines += 1
    except FileNotFoundError:
        print(f"Файл {filename} не найден")
        return

    print(total_lines)
    print(error_lines)
    print(broken_lines)

    with open(filename, encoding="utf-8") as f:
        counts = count_levels(f)
        
    with open(filename, encoding="utf-8") as f:
        errors = top_errors(f, 3)
        
    report_text = format_report(counts, errors)
    
    with open("report.txt", "w", encoding="utf-8") as f:
        f.write(report_text)


if __name__ == "__main__":
    main()
