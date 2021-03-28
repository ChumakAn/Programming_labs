import re

if __name__ == '__main__':
    first_pattern = r"^21.*.php"
    with open('logs.txt', 'r') as log_file:
        file = log_file.readlines()
    count_of_records = 0
    for line in file:

        result = (re.findall(first_pattern, line))

        if not result:
            pass
        else:
            print(result)
            count_of_records += 1
    print(count_of_records)
