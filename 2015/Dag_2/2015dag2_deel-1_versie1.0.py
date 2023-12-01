def read_file(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    return data


def calc_surf_area(all_dimensions):
    all_surf_area = 0
#    for string in all_dimensions:
#        split_dimensions.append(string.split("x"))

    for index, string in enumerate(all_dimensions):
        string = string.split("x")
        # string = [l*w*h]
        string = [eval(i) for i in string] # convert naar int
        surf_area_one = 2 * string[0] * string[1]
        surf_area_two = 2 * string[1] * string[2]
        surf_area_three = 2 * string[0] * string[2]
        dimension = [surf_area_one, surf_area_two, surf_area_three]

        lowest = min(dimension)/2
        wrap_size = sum(dimension) + lowest
        all_surf_area += wrap_size
    return all_surf_area


def calc_ribbon(dimensions):
    all_surf_area = 0

    for index, string in enumerate(dimensions):
        string = string.split("x")
        # string = [l*w*h]
        string = [eval(i) for i in string]  # convert naar int

        string.sort()
        all_surf_area += string[0] * 2 + string[1] * 2

        bow_size = 0
        all_surf_area += string[0] * string[1] * string[2]

    return all_surf_area

if __name__ == "__main__":
    input_data = read_file("input.txt")
    surf_area = calc_surf_area(input_data)
    ribbon_size = calc_ribbon(input_data)
    print("wrapping paper = ", surf_area)
    print("ribbon = ", ribbon_size)