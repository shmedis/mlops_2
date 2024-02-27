import sys
import os
import io

if len(sys.argv) != 2:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython3 change_text_to_numeric.py data-file\n")
    sys.exit(1)

f_input = sys.argv[1]
f_output = os.path.join("data", "stage3", "train.csv")
os.makedirs(os.path.join("data", "stage3"), exist_ok=True)

def process_data(fd_in, fd_out):
    arr_age = []
    arr_education_num = []
    arr_sex = []
    arr_capital_gain = []

    for line in fd_in:
        line = line.rstrip('\n').split(',')
        arr_age.append(line[0])
        arr_education_num.append(line[1])
        arr_sex.append(line[2])
        arr_capital_gain.append(line[3])

    for i in range(len(arr_sex)):
        if arr_sex[i] == 'Male':
            arr_sex[i] = 1
        else:
            arr_sex[i] = 0

    min_length = min(len(arr_age), len(arr_education_num), len(arr_sex), len(arr_capital_gain))
    arr_age = arr_age[:min_length]
    arr_education_num = arr_education_num[:min_length]
    arr_sex = arr_sex[:min_length]
    arr_capital_gain = arr_capital_gain[:min_length]

    for p_age, p_education_num, p_sex, p_capital_gain in zip(arr_age, arr_education_num, arr_sex, arr_capital_gain):
        fd_out.write(f"{p_age},{p_education_num},{p_sex},{p_capital_gain}\n")

with io.open(f_input, encoding="utf8") as fd_in:
    with io.open(f_output, "w", encoding="utf8") as fd_out:
        process_data(fd_in, fd_out)