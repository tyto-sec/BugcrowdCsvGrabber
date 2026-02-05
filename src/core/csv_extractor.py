import csv

def extract_asset(file_path, target_category, target_field):
    assets = set()
    
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = None
        for line in csvfile:
            if line.startswith('programName,'):
                reader = csv.DictReader([line] + csvfile.readlines())
                break
        
        if reader is None:
            return assets
            
        for row in reader:
            if row.get('inScope', 'false').lower() == 'true':
                if row.get('targetCategory', '').lower() == target_category.lower():
                    identifier = row.get(target_field, '').strip()
                    if identifier:
                        assets.add(identifier)
    return assets

