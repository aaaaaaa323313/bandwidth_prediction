

with open('all_file') as f:
    data_set = f.readlines()

data_set = [x.strip() for x in data_set]


for f_name in data_set:
    with open(f_name) as f:
        lines = f.readlines()

    for line in lines:
        line  = line.strip()
        items = line.split(' ')
        v = float(items[4]) / float(items[5])
        if v < 700:
            print v
