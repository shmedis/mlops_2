import sys
import os
import io

if len(sys.argv) != 2:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython3 get_features.py data-file\n")
    sys.exit(1)

f_input = sys.argv[1]
f_output = os.path.join("data", "stage1", "train.csv")
os.makedirs(os.path.join("data", "stage1"), exist_ok=True)

def process_data(fd_in, fd_out):
    fd_in.readline()
    for line in fd_in:
        line = line.rstrip('\n').split(',')
        p_age = line[0]
        p_education_num = line[4]
        p_sex = line[9]
        p_capital_gain = line[10]
        if line[2][0] == '"':
            p_sex = line[9]  
        else:
            p_sex = line[8]
        fd_out.write("{},{},{},{}\n".format(p_age, p_education_num, p_sex, p_capital_gain))

with open(f_input, encoding="utf8") as fd_in:
    with open(f_output, "w", encoding="utf8") as fd_out:
        process_data(fd_in, fd_out)

with open(f_input, encoding="utf8") as fd_in:
    with open(f_output, "w", encoding="utf8") as fd_out:
        process_data(fd_in, fd_out)