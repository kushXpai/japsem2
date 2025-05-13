def groupAndSortOwners(file_owner_dict):
    owner_files = {}

    for file, owner in file_owner_dict.items():
        if owner not in owner_files:
            owner_files[owner] = []
        owner_files[owner].append(file)
    
    for owner in owner_files:
        owner_files[owner].sort()
    
    return owner_files

file_owner_dict = {'Input.txt': 'Albert', 'Code.py': 'Stanley', 'Output.txt': 'Albert', 'btech.txt': 'Albert'}
result = groupAndSortOwners(file_owner_dict)
print(result)