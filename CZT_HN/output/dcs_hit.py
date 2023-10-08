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
            photon_count = 0
            cone_count = 0
            for line in infile:
                columns = line.split()
                event_id = int(columns[1])
                process = columns[22]
                if event_id != previous_event_id:
                    photon_count += 1
                if event_id == previous_event_id and previous_process == 'compt' and process == 'phot':
                    if compt_count == 1:
                        double_compton = True
                    if double_compton:
                        outfile.write(current_row)
                        outfile.write(line)
                        double_compton = False
                        compt_count = 0
                        cone_count +=1
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
    print("Total photons detected by system: ")
    print(photon_count)
    print("Compton Cones: ")
    print(cone_count)

def validate_panel_distance(input_file):
    '''
    Validate panel distance and FOV in the y-direction by examining the position of hits in a GATE generated hit file.

    Parameters:
        input_file: String containing the path of the input file. ".dat"
    '''

    expected_distance = 1.0e2
    with open(input_file,'r') as infile:
        for line in infile:
            columns = line.split()
            y_pos = float(columns[14])
            if abs(y_pos) < expected_distance:
                print("event ID:")
                print(int(columns[1]))
                print("y position:")
                print(y_pos)
                return False
    return True
    
def validate_panel_width(input_file):
    '''
    Validates panel width and FOV in the x-direction by examining the position of hits in a GATE generated hit file.

    Parameters:
        input_file: String containing the path of the input file. ".dat"
    '''

    expected_width = 1.0e2
    with open(input_file,'r') as infile:
        for line in infile:
            columns = line.split()
            x_pos =  float(columns[13])
            if abs(x_pos) > expected_width:
                print("event ID:")
                print(int(columns[1]))
                print("x position:")
                print(x_pos)
                return False
    return True
        
def validate_panel_height(input_file):
    '''
    Validates panel height and FOV in the z-direction by examining the position of hits in a GATE generated hit file.

    Parameters:
        input_file: String containing the path of the input file. ".dat"
    '''

    expected_height = 7.5e1
    with open(input_file,'r') as infile:
        for line in infile:
            columns = line.split()
            z_pos =  float(columns[15])
            if abs(z_pos) > expected_height:
                print("event ID:")
                print(int(columns[1]))
                print("z position:")
                print(z_pos)
                return False
    return True

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

def construct_coincidence_list(input_file, output_file):
    '''
    Takes dcs GATE generated hit file and generates an output of the coincidences. The structure of the output
    file is as follows:

    column 0 -- Energy of first scattered photon
    column 1 -- x position of hit
    column 2 -- y position of hit
    column 3 -- z position of hit
    column 4 -- Energy of the absorbed photon
    column 5 -- x position of hit
    column 6 -- y position of hit
    column 7 -- z position of hit

    Parameters:
        input_file: String containing the path of the input file. ".dat"
        output_file: String containing the path of the output file. ".dat"  
    '''

    with open(input_file, 'r') as infile:
        with open(output_file, 'w') as outfile:
            previous_event_id = -1
            previous_process = None
            for line in infile:
                columns = line.split()
                event_id = int(columns[1])
                process = columns[22]
                if event_id == previous_event_id and previous_process == 'compt' and process == 'phot':
                    outfile.write(f"{previous_columns[11]} {previous_columns[13]} {previous_columns[14]} {previous_columns[15]} {columns[11]} {columns[13]} {columns[14]} {columns[15]}\n")
                previous_event_id = event_id
                previous_process = process
                previous_columns = columns


if __name__ == '__main__':
    debug = True
    input_file = 'partial_Hits.dat'
    slim_hit = 'slim_hit.dat'
    dcs_hit = 'dcs_hit.dat'
    dcs_list = 'dcs.dat'

    # First we will create 
    exclude_rayl_interactions(input_file,slim_hit)
    filter_dcs(slim_hit,dcs_hit)
    construct_coincidence_list(dcs_hit,dcs_list)

    if debug:
        if validate_dcs(dcs_hit):
            print("Data valid")
        else:
            print("error: dcs data invalid")
        if validate_panel_distance(dcs_hit):
            print("Panel Distance correct")
        else:
            print("error: Panel distance not as expected")
        if validate_panel_width(dcs_hit):
            print("Panel Width correct")
        else:
            print("error: Panel width not as expected")
        if validate_panel_height(dcs_hit):
            print("Panel Height correct")
        else:
            print("error: Panel height not as expected")