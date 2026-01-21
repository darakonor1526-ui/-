# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r') as csv_f:
        reader = csv.DictReader(csv_f)
        data = []
        for row in reader:
            data.append(row)


    with open(OUTPUT_FILENAME, 'w') as json_f:
        json.dump(data, json_f, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")