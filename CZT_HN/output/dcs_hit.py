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
                if (columns[22] == 'compt') or (columns[22] == 'phot'):
                    outfile.write(line)

def filter_dcs(input_file, output_file, prompt_energy):
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
            prev_line = None
            compt_count = 0
            photon_count = 0
            DCSc_count = 0
            for line in infile:
                columns = line.split()
                event_id = int(columns[1])
                process = columns[22]
                if event_id != previous_event_id:
                    photon_count += 1
                    if process == 'compt':
                        compt_count += 1
                    else:
                        compt_count = 0
                if event_id == previous_event_id and previous_process == 'compt' and process == 'phot':
                    if compt_count >= 1 and abs(float(columns[11])+float(prev_line.split()[11])-prompt_energy) < 0.010:
                        outfile.write(prev_line)
                        outfile.write(line)
                        compt_count = 0
                        DCSc_count +=1
                    else:
                        compt_count = 0
                elif event_id == previous_event_id and previous_process == 'compt' and process != 'phot':
                    compt_count = 0

                previous_event_id = event_id
                previous_process = process
                prev_line = line
    print("Total events detected by system: ")
    print(photon_count)
    print("DCSc Events: ")
    print(DCSc_count)

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

def validate_dcs(input_file, prompt_energy):
    '''
    Validates the filter_dcs function to confirm whether the dcs events sum up to the gamma energy level.

    Parameters:
        input_file: String containing the path of the input file. ".dat"
    '''

    tolerance = 1e-2
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
        if sum > prompt_energy + tolerance and sum < prompt_energy + tolerance:
            print(event_id)
            print(sum)
            return False

    return True

def construct_coincidence_list(input_file, output_file, prompt_energy, spatialBinSize):
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

    tol = 1e-2
    cone_count = 0

    with open(input_file, 'r') as infile:
        with open(output_file, 'w') as outfile:
            previous_event_id = -1
            previous_process = None
            for line in infile:
                columns = line.split()
                event_id = int(columns[1])
                process = columns[22]
                if event_id == previous_event_id and previous_process == 'compt' and process == 'phot' and (int(columns[19]) == 0):
                    if abs((float(columns[11]) + float(previous_columns[11])) - prompt_energy) < tol:
                        if spatialBinSize:
                            # Create spatial bins
                            previous_columns[13] = spatialBinByVal(previous_columns[13],spatialBinSize)
                            previous_columns[14] = spatialBinByVal(previous_columns[14],spatialBinSize)
                            previous_columns[15] = spatialBinByVal(previous_columns[15],spatialBinSize)
                            columns[13] = spatialBinByVal(columns[13],spatialBinSize)
                            columns[14] = spatialBinByVal(columns[14],spatialBinSize)
                            columns[15] = spatialBinByVal(columns[15],spatialBinSize)

                        outfile.write(f"{previous_columns[11]} {previous_columns[13]} {previous_columns[14]} {previous_columns[15]} {columns[11]} {columns[13]} {columns[14]} {columns[15]}\n")
                        cone_count += 1
                previous_event_id = event_id
                previous_process = process
                previous_columns = columns

    print("Compton Cones: ")
    print(cone_count)

def spatialBinByVal(coord, spatialBinSize):
    return float(coord) - float(coord) % spatialBinSize + spatialBinSize/2


if __name__ == '__main__':
    debug = True
    input_file = 'GaPs_RS2023Hits.dat'
    slim_hit = 'slim_hit.dat'
    dcs_hit = 'dcs_hit.dat'
    dcs_list = 'test.dat'

    prompt_energy = 1.077
    spatialBin = 0

    # First we will create 
    #exclude_rayl_interactions(input_file,slim_hit)
    filter_dcs(input_file,dcs_hit,prompt_energy)
    construct_coincidence_list(dcs_hit,dcs_list,prompt_energy,spatialBin)

    if debug:
        if validate_dcs(dcs_hit,prompt_energy):
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