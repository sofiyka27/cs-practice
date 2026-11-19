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

def merge_by_key(rows: list[dict], extra: dict, key: str = 'id') -> list[dict]:
    result = []
    for row in rows:
        new_row = row.copy()
        
        row_id = row.get(key)
        
        if row_id in extra:
            new_row.update(extra[row_id])
            
        result.append(new_row)
        
    return result

def records_to_json(records: list[dict]) -> str:
    def format_val(v):
        if isinstance(v, str):
            return f'"{v}"'
        if isinstance(v, bool):
            return 'true' if v else 'false'
        if v is None:
            return 'null'
        return str(v)

    def format_dict(d, indent_level):
        indent = "  " * indent_level
        next_indent = "  " * (indent_level + 1)
        if not d:
            return "{}"
        
        lines = []

        for k in sorted(d.keys()):
            v = d[k]
            if isinstance(v, dict):
                val_str = format_dict(v, indent_level + 1)
            elif isinstance(v, list):
                
                val_str = "[\n" + ",\n".join([next_indent + format_val(item) for item in v]) + "\n" + indent + "]"
            else:
                val_str = format_val(v)
            
            lines.append(f'{next_indent}"{k}": {val_str}')
        
        return "{\n" + ",\n".join(lines) + "\n" + indent + "}"
        
    if not records:
        return "[]"
        
    res = "[\n"
    items = []
    for record in records:
        items.append("  " + format_dict(record, 1))
    res += ",\n".join(items) + "\n]"
    
    return res
        