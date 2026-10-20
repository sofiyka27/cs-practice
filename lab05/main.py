import logstats

def main():
    with open(filename, encoding="utf-8") as log_file:
        counts = logstats.count_levels(log_file)
    
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
