def exclude_rayl_interactions(input_file, output_file):
    with open(input_file, 'r') as infile:
        with open(output_file, 'w') as outfile:
            for line in infile:
                columns = line.split()
                if columns[22] != 'Rayl':
                    outfile.write(line)

if __name__ == '__main__':
    input_file = 'input.dat'
    output_file = 'output.dat'
    exclude_rayl_interactions(input_file, output_file)