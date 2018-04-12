from os import listdir
from os.path import isfile, join

# Make sure the input and output directories exist.
# All files in the input directory will be processed and assumed to have a three letter extension
input_dir = join('machine' , 'data', 'lookup-3bit')
output_dir = 'testtesttest'

input_files = [f for f in listdir(input_dir) if isfile(join(input_dir, f))]

for filename in input_files:
    input_file = open(join(input_dir, filename), 'r')
    output_source_file = open(join(output_dir, filename[:-4] + '-source' + filename[-4:]), 'w')
    output_target_file = open(join(output_dir, filename[:-4] + '-target' + filename[-4:]), 'w')

    for line in input_file:
        line = line.rstrip()

        source, target = line.split('\t')

        output_source_file.write(source + '\n')
        output_target_file.write(target + '\n')

    input_file.close()
    output_source_file.close()
    output_target_file.close()