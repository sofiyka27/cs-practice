def csv_to_records(text: str) -> list[dict]:
    if not text.strip():
        return[]

    lines = text.strip().split('\n')
    headers = lines[0].split(',')

    records = []
    for line in lines[1:]:
        values = line.split(',')
        record = dict(zip(headers,values))
        records.append(record)
        
        return records 

def parse_settings(lines:list[str]) -> dict:
    result = {}
    current_key = None

    for line in lines:
        if not line.strip():
            continue

        if line.strip().startswith('-'):
            if current_key is not None:
                if not isinstance(result.get(current_key), list):
                    result[current_key] = []

                val = line.strip()[2:].strip()

                if val.lower() in ('true','yes'):
                    converted_val = True
                elif val.lower() in ('false','no'):
                    converted_val = False
                else:
                    try:
                        if '.' in val:
                            converted_val = float(val)
                        else: 
                            converted_val = int(val)
                    except ValueError:
                        converted_val = val
                result[current_key].append(converted_val)

            continue
        
        if ':' in line:
            parts = line.split(':',1)
            key = parts[0].strip()
            val = parts[1].strip()

            current_key = key

            if val == "":
                if val.lower() in ('true','yes'):
                    converted_val = True
                elif val.lower() in ('false','no'):
                    converted_val = False
                else:
                    try:
                        if '.' in val:
                            converted_val = float(val)
                        else: 
                            converted_val = int(val)
                    except ValueError:
                        converted_val = val
                result[key] = converted_val
    return result

    
        