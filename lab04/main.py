import sys

from stats import read_valid, average_by_city, warmest_city

def main():
    lines = sys.stdin.read().splitlines()
    total_lines = len([line for line in lines if line.strip()])
    valid_records = read_valid(lines)
    parsed_count = len(valid_records)
    skipped_count = total_lines - parsed_count
    averages = average_by_city(valid_records)

    if averages:
        best_city = warmest_city(valid_records)
        best_temp = averages[best_city]
    else:
        best_temp = 0.0

    print(parsed_count)
    print(skipped_count)
    print(f"{best_temp:.1f}")

if __name__ == "__main__":
    main()