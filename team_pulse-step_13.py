# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: TeamPulse
class SearchEngine:
    def __init__(self, data):
        self.data = data
    
    def search(self, query_fields=None):
        if not isinstance(query_fields, dict) or len(query_fields) == 0:
            return []
        
        results = list(self.data.values())
        for field_name, value in query_fields.items():
            lower_value = value.lower()
            filtered_results = []
            
            for record_id, record_data in results.items():
                if isinstance(record_data.get(field_name), str):
                    search_str = record_data[field_name].lower()
                    if lower_value in search_str:
                        filtered_results.append((record_id, record_data))
                
                elif isinstance(record_data.get(field_name), list):
                    for item in record_data[field_name]:
                        if isinstance(item, str) and lower_value in item.lower():
                            filtered_results.append((record_id, record_data))
                            break
                
                else:
                    try:
                        search_val = str(record_data.get(field_name)).lower()
                        if lower_value in search_val:
                            filtered_results.append((record_id, record_data))
                    except (ValueError, TypeError):
                        pass
            
            results = filtered_results
        
        return [item[1] for item in results]
