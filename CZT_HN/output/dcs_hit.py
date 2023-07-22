def exclude_rayl_interactions(input_file, output_file):
    '''
    Outputs a ".dat" file that excludes all Rayleigh events. Future considerations should include 'eIoni' and 'msc' events.
    
    Parameters:
        input_file: String containing the path of the input file. ".dat"
        output_file: String containing the path of the output file. ".dat"
    '''
    with open(input_file, 'r') as infile:
        with open(output_file, 'w') as outfile:
            for line in infile:
                columns = line.split()
                if columns[22] != 'Rayl':
                    outfile.write(line)

def filter_dcs(input_file, output_file):
    '''
    Filters a ".dat" hit file and outputs only double compton scattering events.

    Paramters:
        input_file: String containing the path of the input file. ".dat"
        output_file: String containing the path of the output file. ".dat"
    '''
    with open(input_file, 'r') as infile:
        with open(output_file, 'w') as outfile:
            previous_event_id = -1
            previous_process = None
            current_row = None
            double_compton = False
            compt_count = 0
            for line in infile:
                columns = line.split()
                event_id = int(columns[1])
                process = columns[22]
                if event_id == previous_event_id and previous_process == 'compt' and process == 'phot':
                    if compt_count == 1:
                        double_compton = True
                    if double_compton:
                        outfile.write(current_row)
                        outfile.write(line)
                        double_compton = False
                        compt_count = 0
                    else:
                        compt_count = 0
                elif event_id != previous_event_id and previous_process == 'compt' and process == 'compt':
                    compt_count = 1
                    double_compton = False
                else:
                    double_compton = False
                    if process == 'compt':
                        compt_count += 1
                previous_event_id = event_id
                previous_process = process
                current_row = line

def validate_dcs(input_file):
    '''
    Validates the filter_dcs function to confirm whether the dcs events sum up to the gamma energy level.

    Parameters:
        input_file: String containing the path of the input file. ".dat"
    '''
    tolerance = 1e-2
    target_energy = 0.909
    with open(input_file, 'r') as infile:
        event_ids = set()
        sums = {}
        for line in infile:
            columns = line.split()
            event_id = int(columns[1])
            energy = float(columns[11])
            if event_id in event_ids:
                sums[event_id] += energy
            else:
                sums[event_id] = energy
                event_ids.add(event_id)

    for event_id, sum in sums.items():
        if sum > target_energy + tolerance and sum < target_energy + tolerance:
            print(event_id)
            print(sum)
            return False

    return True

if __name__ == '__main__':
    input_file = 'partial_Hits.dat'
    slim_hit = 'slim_hit.dat'
    dcs_hit = 'dcs_hit.dat'
    exclude_rayl_interactions(input_file,slim_hit)
    filter_dcs(slim_hit,dcs_hit)

    if validate_dcs(dcs_hit):
        print("Data valid")
    else:
        print("error: dcs data invalid")