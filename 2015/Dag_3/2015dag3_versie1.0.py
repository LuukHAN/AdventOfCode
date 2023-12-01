def read_file(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    return data


if __name__ == "__main__":
    input_data = read_file("input.txt")
    print(input_data)
