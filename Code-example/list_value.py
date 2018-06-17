data = "Python is a best language"

def create_value(data_str):
    input_data = data_str.split()
    result = []
    for index, element in enumerate(input_data):
        result.append((index + 1, element))
    return result

if __name__ == "__main__":
    print(create_value(data))
