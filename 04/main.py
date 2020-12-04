
input_list = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        input_list.append(line.strip())

def parse_line_input(line):
    hash_fields = {}
    fields = line.split(" ")
    for field in fields:
        field_map = {}
        _field = field.split(":")
        hash_fields[_field[0]] = _field[1]
    return hash_fields

def is_in_list(element, _list):
    is_in_list = False
    for _list_el in _list:
        if element == _list_el:
            is_in_list = True
    return is_in_list

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def parse_input(mylist):
    passenger_fields = []
    person_fields = {}
    mylist.append('')
    for idx, line in enumerate(mylist):
        if line == '':
            passenger_fields.append(person_fields)
            person_fields = {}
        else:
            fields = parse_line_input(line)
            for key in fields:
                person_fields[key] = fields[key]
    return passenger_fields

def validate_field(field, field_value):
    if field == 'byr':
        if RepresentsInt(field_value):
            field_value_int = int(field_value)
            return field_value_int >= 1920 and field_value_int <= 2002 and len(field_value) == 4
    elif field == 'iyr':
        if RepresentsInt(field_value):
            field_value_int = int(field_value)
            return field_value_int >= 2010 and field_value_int <= 2020 and len(field_value) == 4
    elif field == 'eyr':
        if RepresentsInt(field_value):
            field_value_int = int(field_value)
            return field_value_int >= 2020 and field_value_int <= 2030 and len(field_value) == 4
    elif field == 'hgt':
        if field_value[-2:] == 'cm':
            return int(field_value[:-2]) >= 150 and int(field_value[:-2]) <= 193
        elif field_value[-2:] == 'in':
            return int(field_value[:-2]) >= 59 and int(field_value[:-2]) <= 76
    elif field == 'hcl':
        if len(field_value) != 7:
            return False
        if field_value[0] != '#':
            return False
        for char in field_value[1:]:
            valid_number = False
            if RepresentsInt(char):
                if is_in_list(int(char), [0,1,2,3,4,5,6,7,8,9]):
                    valid_number = True
            valid_char = False
            if is_in_list(char, ['a', 'b', 'c', 'd', 'e', 'f']):
                valid_char = True
            return valid_char or valid_number
    elif field == 'ecl':
        return is_in_list(field_value, ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
    elif field == 'pid':
        return len(field_value) == 9

def count_valid_passengers(passenger_fields, valid_fields):
    valid_passwords = 0
    for passenger in passenger_fields:
        valid_pass = True
        for required_field in valid_fields:
            if not required_field in passenger:
                valid_pass = False
            if required_field in passenger:
                if not validate_field(required_field, passenger[required_field]):
                    print( required_field + " not valid field for value " + passenger[required_field])
                    valid_pass = False
        if valid_pass:
            valid_passwords += 1
    return valid_passwords

def part_one(mylist):
    valid_fields = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'hgt', 'iyr']
    passenger_fields = parse_input(mylist)
    print(count_valid_passengers(passenger_fields, valid_fields))

def main():
    part_one(input_list)

main()