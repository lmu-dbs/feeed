import json
def compare_json(file1, file2):
    with open(file1, 'r') as f:
        json_data1 = json.load(f)

    with open(file2, 'r') as f:
        json_data2 = json.load(f)

    return json_data1 == json_data2

if __name__ == "__main__":
    file1 = "output.json"
    file2 = "expected_output.json"
    
    if compare_json(file1, file2):
        print("JSON files are identical")
    else:
        print("JSON files differ")
        exit(1)
