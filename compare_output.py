import json
from json_diff import diff

def compare_json(file1, file2):
    with open(file1, 'r') as f:
        json_data1 = json.load(f)

    with open(file2, 'r') as f:
        json_data2 = json.load(f)

    differences = diff(json_data1, json_data2, syntax='explicit')

    return differences

if __name__ == "__main__":
    file1 = "output.json"
    file2 = "expected_output.json"
    
    differences = compare_json(file1, file2)

    if not differences:
        print("JSON files are identical")
    else:
        print("JSON files differ:")
        print(differences)
        exit(1)
