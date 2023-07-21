#!/usr/bin/env python
# coding: utf-8

# In[1]:


# This code is for reading the Hit File from the simulation

# Input:  The output of the Gate
# Output: The processed Hit file with

# output 1 ----> the Slim Hit file
#   Creating the Slim Hit File with 11 columns with this structure: 
#   "Event ID", "Time Slice", "Gamma ID", "Node(detector)", "X", "Y", "Z", "Time", "Edep", "type", "Gamma Source"

# output 2 ----> the Compton PHotoElectric (CP) Counts 
#   Creating the CP Count File with 7 columns with this structure
#   "Event ID", "Time Slice", "Gamma ID", "Node (detector)", "Compton", "PhotoElectric"

# output 3 ----> the Compron PhotoElectric (CP) Table
#   Creating the CP Table with 8 columns with this structure
#   Total, 0C/1P, 1C/1P, 2C/1P, 3C/1P, 4C/1P, (more than 4c and 1p) #C/1P, and (any c and more than 1p) #C/#P

# output 4 ----> the Coincidence Pairs
#   Creating the Coin Pair File with 10 columns with this structure
#   "Event ID", "Time Slice", "Gamma ID 1", "Gamma ID 2", "X1", "Y1", "Z1", "X2", "Y2", "Z2"

# output 5 ----> the Double Compton Scatter (DCS) events
#   Creating the DCS File with 4 columns with this structure
#   "Event ID", "Time Slice", "Gamma ID 1", "Gamma ID 2"

# output 6 ----> the Double Compton Scatter (DCS) Pairs
#   Creating the DCS Position File with 16 columns with this structure
#   "Event ID", "Time Slice", "Gamma ID 1", "Gamma ID 2", "XC1", "YC1", "ZC1", "XP1", "YP1", "ZP1", "XC2", "YC2",
#   "ZC2", "XP2", "YP2", "ZP2"

# output 7 ----> the Prompt vs Aniihilation table
#   Creating the PvsA table with 26 rows for each event
#   Gamma ID: 0 as prompt, 1 and 2 as the coincidence pair of the annihilation 


#   Structure of Raw HIT file (Input of this code):
#   Column 0  : Time Slice
#   Column 1  : Event ID
#   Column 2  : ID of the primary particle whose descendant generated this hit
#   Column 3  : ID of the source which emitted the primary particle
#   Column 4  : Volume IDs at each level of the hierarchy of a system, so the number of columns depends on the 
#               system used (columns 4 to 10).
#   Column 10 : Time Stamp
#   Column 11 : Energy Deposited by the Hit (Edep)
#   Column 12 : Range of particle which has generated the Hit
#   Column 13 : X position
#   Column 14 : Y position
#   Column 15 : Z position
#   Column 16 : Code of the particle which has generated the Hit (11 for Electrons & 22 for Photons) 
#   Column 17 : ID of the particle which has generated the Hit
#   Column 18 : ID of the mother of the event
#   Column 19 : Gamma ID
#   Column 20 : Number of Compton interactions in phantoms before reaching the detector
#   Column 21 : Number of Rayleigh interactions in phantoms before reaching the detector
#   Column 22 : Name of the process (Compton, PhotoElectric, RayLight, MSC, eIoni)
#   Column 23 : Name of the last volume where a Compton effect occurred
#   Column 24 : Name of the last volume where a Rayleigh effect occurred


# In[2]:


# Import Libraries
import numpy as np
import matplotlib.pyplot as plt
import csv
import os

# The Path to the Raw Hit File
# Greg Hit File:
# Raw_Hit_Path = '/Users/kimia/Desktop/Prompt Gamma/Hit Processing/input/input_Greg/point_source_511kev_10s_Hits.dat'
# Greyson Hit File
# Raw_Hit_Path = '/Users/kimia/Desktop/Prompt Gamma/Hit Processing/input/input_Greyson/Zr89Hit.dat'
# Greyson last version Hit File
Raw_Hit_Path = '/Users/kimia/Desktop/Prompt Gamma/Hit Processing/input/input_Greyson-new/Zr89Hit_simple.dat'

# The path to the desired outputs
output_path = '/Users/kimia/Desktop/Prompt Gamma/Hit Processing/output'


# In[3]:


# The function that reads the Raw Hit File and generates the Slim Hit File as the output
def Slim_Hit(Raw_Hit_Path, max_hits=-1):
    SlimHits= []
    raw_hits_count = 0
    slim_hits_count = 0
    number_of_cols = 25   # based on GATE output for cylindralPET system
    gamma = '22'          # GEANT4 code
    writeBuffer = []
    eventIDLast = -1
    filename = 'Slim_Hits.csv'
    path = os.path.join(output_path, filename)
    print(f'Processing the Slim Hit File with the Raw Hit File:... \n',end='')
#     Creating the Slim Hit File with 11 columns with this structure: 
#     'Event ID', 'Time Slice', 'Gamma ID', 'Node(detector)', 'X', 'Y', 'Z', 'Time', 'Edep', 'type', 'Gamma Source'
    header = ['Event ID', 'Time Slice', 'Gamma ID', 'Node(detector)', 'X', 'Y', 'Z', 'Time', 'Edep', 'type',
            'Gamma Source']
    
    def my_sort(row):
        return(row[0], row[1], row[2], row[7])
    
#     Reading the Raw Hit File and selecting the events. Check if a row is different or has a different structure
#     Only events generated from Photons (column 16 = '22')
#     Without phantom scatter (column 20, column 21 = '0' )
#     Not 'Rayl' or 'eIoni' events 
    with open(Raw_Hit_Path,'r') as HitFile, open(path, 'w', newline='') as SlimFile:
        writer = csv.writer(SlimFile)
        writer.writerow(header)
        for line in HitFile:
            if max_hits != -1 and raw_hits_count >= max_hits: 
                break
            row = line.split()
            if (len(row) != number_of_cols): 
                print(f'Number of items in event {raw_hits_count} is differnt {row}\n')
                continue
            if (row[16]==gamma and row[20]=='0' and row[21]=='0' and row[22]!='eIoni' and row[22]!='Rayl' 
                and row[22]!='msc'):
                slim_hits_count = slim_hits_count + 1
                data =   list(map(int,   row[0:10]))  \
                       + list(map(float, row[10:16])) \
                       + list(map(int,   row[16:22])) \
                       + list(map(str,   row[22:]))
                
                if (row[19]=='0' or row[19]==0): 
                    data.append('Prompt') 
                else: 
                    data.append('Annihilation')

                slimRow = [ data[1],   # Column 0  : Event ID 
                            data[0],   # Column 1  : Time Slice 
                            data[19],  # Column 2  : Gamma ID
                            data[5],   # Column 3  : Node (Detector)
                            data[13],  # Column 4  : X position
                            data[14],  # Column 5  : Y position 
                            data[15],  # Column 6  : Z position
                            data[10],  # Column 7  : Time Stamp
                            data[11],  # Column 8  : Edep as the amount of Energy deposited
                            data[22],  # Column 9  : Interaction type
                            data[25]]  # Column 10 : Gamma Source
                
#                 Sorting and Writing:
#                 Column 0  Event ID    rows are sorted by Event ID
#                 Column 1  Time Slice  rows with the same Event ID, are sorted by Time Slice
#                 Column 2  Gamma ID    rows with the same Event ID, Time Slice, are sorted by Gamma ID
#                 Column 7  Time Stamp  rows with the same Event ID, Time Slice, Gamma ID are sorted by Time Stamp
                eventIDCurrent = slimRow[0]
                if eventIDCurrent == eventIDLast or eventIDLast == -1:
                    writeBuffer.append(slimRow)
                    eventIDLast = eventIDCurrent
                else:
                    if (len([writeBuffer[0]]) > 1):
                        writeBuffer = sorted(writeBuffer, key=my_sort)
                        for slimRow in writeBuffer:
                            writer.writerow(slimRow)
                    else:
                        writer.writerow(slimRow)

                    writeBuffer = slimRow
                    eventIDLast == eventIDCurrent

            raw_hits_count = raw_hits_count +1
            if raw_hits_count % 1000000 == 0: print(f'Processed {raw_hits_count} lines')
                
    print('Done processing')
    print(f'The lenght of the events in the Raw Hit File is {raw_hits_count} \n', 
          f'Each gamma ray in the Raw Hit File has {number_of_cols} columns \n', 
          f'The lenght of the events in the Slim Hit File is {slim_hits_count} \n', 
          f'Each gamma ray in the Slim Hit File has {len(slimRow)} columns \n', 
          f'The Slim Hit File is saved as Slim_Hit.csv \n')
                
    print("Reading Slim Hits into memory...", end='')
    with open(path, 'r') as slimFile:
        SlimHits.append(header)
        for idx, row in enumerate(slimFile):
            if idx == 0: continue
            row = row.split(',')
            data =    list(map(int,   row[0:4]))  \
                    + list(map(float, row[4:9]))  \
                    + list(map(str,   row[9:]))
            SlimHits.append(data)
    print('done')

    return (SlimHits)


# In[4]:


def CP_Count(Slim_Hit_File):
    cp = []
    CP_Count_File = []
    filename = 'CP_Count.csv'
    path = os.path.join(output_path, filename)
    print('Generating the CP Count File with the Slim Hit File:...', end='')
#     Creating the CP Count File with 7 columns with this structure
#     'Event ID', 'Time Slice', 'Gamma ID', 'Node (detector)', 'Compton', 'PhotoElectric'
    header = ['Event ID', 'Time Slice', 'Gamma ID', 'Node (detector)', 'Compton', 'PhotoElectric']
    CP_Count_File.append(header)
    
    def my_sort(row):
        return(row[0], row[1], row[2], row[3])

#     Counting different types of events for each gamma ray: 
#     Adding 1 to 'c' variable for Compton events and 1 to 'p' variable for PhotoElectric events 
    def event_type(row):
        c = int(0)
        p = int(0)
        if row[9]== 'Compton' or row[9]=='compton' or row[9]=='Compt' or row[9]=='compt':
            c = c + 1
        if row[9]=='PhotoElectric' or row[9]=='photoelectric' or row[9]=='Phot' or row[9]=='phot':
            p = p + 1
        return (c,p)
    
    for i in range(1, len(Slim_Hit_File)):
        row = Slim_Hit_File[i]
        c,p = event_type(row)
        temp = []
        temp.append(row[0])
        temp.append(row[1])
        temp.append(row[2])
        temp.append(row[3])
        temp.append(c)
        temp.append(p)
        l = len(cp) - 1
        T = 0
        while T==0:
            if l>=0:
                if cp[l][0]==temp[0] and cp[l][1]==temp[1] and cp[l][2]==temp[2] and cp[l][3]==temp[3]:
                    cp[l][4] = cp[l][4] + temp[4]
                    cp[l][5] = cp[l][5] + temp[5]
                    T = 1
                    break
                elif cp[l][0]<temp[0] or cp[l][1]<temp[1] or cp[l][2]<temp[2]:
                    break
                else:
                    l = l - 1
            if T==1 or l<0:
                break
        if T==0:
            cp.append(temp)

    for i in range(0,len(cp)):
        temp = cp[i]
        CP_Count_File.append(temp)

    CP_Count_File[1:] = sorted(CP_Count_File[1:], key=my_sort)
    
    print('Done processing')
    print(f'The lenght of the Compton and PhotoElectric events in CP Count File is {len(CP_Count_File)-1} \n',
          f'The CP Count File is saved as CP_Count.csv \n')
    
    print('Reading Compton PhotoElectric events into memory...', end='')
    with open(path, mode='w', newline='') as f:
        writer = csv.writer(f)
        for i in CP_Count_File:
            writer.writerow(i)
    print('done')
    
    return (CP_Count_File)


# In[5]:


def CP_Table(CP_Count_File):
    cnt_w = 0
    row_w = []
    CP_Table_File = []
    filename = 'CP_Table.csv'
    path = os.path.join(output_path, filename)
    print('Generating the CP Table with the CP Count File:...\n', end='')
#     Creating the CP Table with 8 columns with this structure
#     Total, 0C/1P, 1C/1P, 2C/1P, 3C/1P, 4C/1P, (more than 4c and 1p) #C/1P, and (any c and more than 1p) #C/#P
    header = ['Total', '0C / 1P', '1C / 1P', '2C / 1P', '3C / 1P', '4C / 1P', '#C / 1P', '#C / #P']
    CP_Table_File.append(header)
    current_counts = [0, 0, 0, 0, 0, 0, 0, 0]
    CP_Table_File.append(current_counts)
    
    for i in range(1, len(CP_Count_File)):
        row = CP_Count_File[i]
        CP_Table_File[1][0] = CP_Table_File[1][0] + 1 
        if row[5]>1:
            CP_Table_File[1][7] = CP_Table_File[1][7] + 1
            cnt_w = cnt_w + 1
            row_w.append(i)
            print(f'wrong Gamma rays in row {row} \n')
        elif row[4]==0:
            CP_Table_File[1][1] = CP_Table_File[1][1] + 1
        elif row[4]==1:
            CP_Table_File[1][2] = CP_Table_File[1][2] + 1
        elif row[4]==2:
            CP_Table_File[1][3] = CP_Table_File[1][3] + 1
        elif row[4]==3:
            CP_Table_File[1][4] = CP_Table_File[1][4] + 1
        elif row[4]==4:
            CP_Table_File[1][5] = CP_Table_File[1][5] + 1
        else: 
            CP_Table_File[1][6] = CP_Table_File[1][6] + 1

    print('Done processing')
    print(f'The wrong rows are: \n {row_w}', f'\nThere are {str(cnt_w)} number of rows with wrong gamma rays \n',
          f'Number of total true events in the CP Table File is {CP_Table_File[1][0]} \n',
          f'The CP Table File is saved as CP_Table.csv \n')
    
    print('Reading the Compton PhotoElectric Table into memory...', end='')
    with open(path, mode='w', newline='') as f:
        writer = csv.writer(f)
        for i in CP_Table_File:
            writer.writerow(i)
    print('done')
    
    return (CP_Table_File)


# In[6]:


def Coin_Pair(Slim_Hit_File, CP_Count_File):
    idx = 1
    x1, y1, z1 = 0, 0, 0 
    x2, y2, z2 = 0, 0, 0 
    Coin_Pair_File = []
    filename = 'Coin_Pair.csv'
    path = os.path.join(output_path, filename)
    print('Generating the Coincidence Pair File with the Slim Hit File and CP Count File:...\n', end='')
#     Creating the Coin Pair File with 10 columns with this structure
#     'Event ID', 'Time Slice', 'Gamma ID 1', 'Gamma ID 2', 'X1', 'Y1', 'Z1', 'X2', 'Y2', 'Z2'
    header = ['Event ID', 'Time Slice', 'Gamma ID 1', 'Gamma ID 2', 'X1', 'Y1', 'Z1', 'X2', 'Y2', 'Z2']
    Coin_Pair_File.append(header)
    
    def xyzPair(row, idx):
        T = 0
        for i in range(idx,len(Slim_Hit_File)):
            temp = Slim_Hit_File[i]
            if temp[0]<row[0] or temp[1]<row[1]:
                continue
            elif temp[0]==row[0] and temp[1]==row[1] and temp[2]==row[2] and T==0:
                x = temp[4]
                y = temp[5]
                z = temp[6]
                T = 1
                idx = i
                break
            elif temp[0]>row[0] or temp[1]>row[1] or temp[2]>row[2] or T==1:
                break
        return(x, y, z, idx)
    
    for i in range(1, len(CP_Count_File)-1):
        row1 = CP_Count_File[i]
        row2 = CP_Count_File[i+1]
        if row1[0]==row2[0] and row1[1]==row2[1] and row1[2]!=row2[2] and row1[2]!=0 and row2[2]!=0:
            row = []
            row.append(row1[0])  
            row.append(row1[1])
            row.append(row1[2])
            x1, y1, z1, idx = xyzPair(row, idx)
            row = []
            row.append(row1[0])  
            row.append(row1[1])
            row.append(row2[2])
            x2, y2, z2, idx = xyzPair(row, idx)
            row = []
            row.append(row1[0])  
            row.append(row1[1])
            row.append(row1[2])
            row.append(row2[2])
            row.append(x1)
            row.append(y1)
            row.append(z1)
            row.append(x2)
            row.append(y2)
            row.append(z2)
            Coin_Pair_File.append(row)
            
    print('Done processing')
    print(f'The lenght of Coincidence Pair in Coin Pair File is {len(Coin_Pair_File)-1} \n',
          f'The Coin Pair File is saved as Coin_Pair.csv \n')
    
    print('Reading the conincidence pair file into memory...', end='')
    with open(path, mode='w', newline='') as f:
        writer = csv.writer(f)
        for i in Coin_Pair_File:
            writer.writerow(i)
    print('done')

    return (Coin_Pair_File)


# In[7]:


def DCS(CP_Count_File):
    DCS_File = []
    filename = 'DCS.csv'
    path = os.path.join(output_path, filename)
    print('Generating the DCS File (1 Compton scatter on both sides) with the CP Count File:...\n', end='')
#     Creating the DCS File with 4 columns with this structure
#     'Event ID', 'Time Slice', 'Gamma ID 1', 'Gamma ID 2'
    header = ['Event ID', 'Time Slice', 'Gamma ID 1', 'Gamma ID 2']
    DCS_File.append(header)
    
    for i in range(1,len(CP_Count_File)-1):
        temp = CP_Count_File[i]
        if temp[4]==1 and temp[5]==1:
            row = []
            row.append(temp[0])
            row.append(temp[1])
            row.append(temp[2])
            j = i + 1
            while j<len(CP_Count_File) and j!=0 and CP_Count_File[j][0]==temp[0] and CP_Count_File[j][1]==temp[1]:
                temp1 = CP_Count_File[j]
                if temp1[0]==temp[0] and temp1[1]==temp[1] and temp1[2]!=temp[2] and temp1[2]!=0 and temp[2]!=0:
                    if temp1[4]==1 and temp1[5]==1:
                        row.append(temp1[2])
                elif temp1[0]>temp[0] or temp1[1]>temp[1]:
                    j = 0
                    break
                if j!=0:
                    j = j + 1
            if len(row)==4:
                DCS_File.append(row)
                
    print('Done processing')
    print(f'The lenght of DCS File is {len(DCS_File)-1} \n',f'The DCS File is saved as DCS.csv \n')
    
    print('Reading the true coin file with 1c 1p events into memory...', end='')
    with open(path, mode='w', newline='') as f:
        writer = csv.writer(f)
        for i in DCS_File:
            writer.writerow(i)
    print('done')
    
    return(DCS_File)


# In[8]:


def DCS_Pos(Slim_Hit_File, DCS_File):
    idx=1
    xc1, yc1, zc1, xp1, yp1, zp1 = 0, 0, 0, 0, 0, 0
    xc2, yc2, zc2, xp2, yp2, zp2 = 0, 0, 0, 0, 0, 0
    DCS_Pos_File = []
    filename = 'DCS_Pos.csv'
    path = os.path.join(output_path, filename)
    print('Generating the Position DCS File with the Slim Hit File and DCS File:...\n', end='')
#     Creating the DCS Position File with 16 columns with this structure
#     'Event ID', 'Time Slice', 'Gamma ID 1', 'Gamma ID 2', 'XC1', 'YC1', 'ZC1', 'XP1', 'YP1', 'ZP1', 
#     'XC2', 'YC2', 'ZC2', 'XP2', 'YP2', 'ZP2'
    header = ['Event ID', 'Time Slice', 'Gamma ID 1', 'Gamma ID 2', 'XC1', 'YC1', 'ZC1', 'XP1', 'YP1', 'ZP1', 
              'XC2', 'YC2', 'ZC2', 'XP2', 'YP2', 'ZP2']
    DCS_Pos_File.append(header)
    
#     row = [Event ID', 'Time Slice', 'Gamma ID']
    def xyz_cp(row, idx):
        Tc, Tp = 0, 0
        for i in range(idx, len(Slim_Hit_File)):
            temp = Slim_Hit_File[i]
            if temp[0]==row[0] and temp[1]==row[1] and temp[2]==row[2]:
                if Tc==0:
                    xc = temp[4]
                    yc = temp[5]
                    zc = temp[6]
                    Tc = 1
                elif Tp==0:
                    xp = temp[4]
                    yp = temp[5]
                    zp = temp[6]
                    Tp = 1
                    idx = i
                    break
            elif Tc==1 and Tp==1:
                break
        return (xc, yc, zc, xp, yp, zp, idx)
    
    for i in range(1, len(DCS_File)):
        row = DCS_File[i]
        row1 = []
        row1.append(row[0])
        row1.append(row[1])
        row1.append(row[2])
        xc1, yc1, zc1, xp1, yp1, zp1, idx = xyz_cp(row1, idx)
        row.append(xc1)
        row.append(yc1)
        row.append(zc1)
        row.append(xp1)
        row.append(yp1)
        row.append(zp1)
        row2 = []
        row2.append(row[0])
        row2.append(row[1])
        row2.append(row[3])
        xc2, yc2, zc2, xp2, yp2, zp2, idx = xyz_cp(row2, idx)
        row.append(xc2)
        row.append(yc2)
        row.append(zc2)
        row.append(xp2)
        row.append(yp2)
        row.append(zp2)
        DCS_Pos_File.append(row)
    
    print('Done processing')
    print(f'The lenght of DCS Pos File is {len(DCS_Pos_File)-1} \n',
          f'The DCS Pos File is saved as DCS_Pos.csv \n')
        
    print('Reading the DCS position file into memory...', end='')
    with open(path, mode='w', newline='') as f:
        writer = csv.writer(f)
        for i in DCS_Pos_File:
            writer.writerow(i)
    print('done')
            
    return(DCS_File)


# In[9]:


def PvsA(CP_Count_File):
    total = 0    
    PvsA_File = []
    filename = 'PvsA.csv'
    path = os.path.join(output_path, filename)
    print('Creating a table for prompt/annihilation and Compton/PhotoElectric events:... \n', end='')
#     Creating the PvsA table with 26 rows for each event
#     Gamma ID: 0 as prompt, 1 and 2 as the coincidence pair of the annihilation 
    header = [' ', 'Annihilation photon 1', 'Annihilation photon 2', 'Prompt gamma', 'Sensitivity (%)']     
    PvsA_File.append(header)
    row = ['type 1', 'PhotoElectric', 'PhotoElectric', 'Compton', 0]      # row 1: 112
    PvsA_File.append(row)
    row = ['type 2', 'PhotoElectric', 'PhotoElectric', 'None Compton', 0] # row 2: 111, 110
    PvsA_File.append(row)
    row = ['type 3', 'PhotoElectric', 'Compton', 'Compton', 0]            # row 3: 122, 212
    PvsA_File.append(row)
    row = ['type 4', 'PhotoElectric', 'Compton', 'None Compton', 0]       # row 4: 121, 120, 211, 210
    PvsA_File.append(row)
    row = ['type 5', 'Compton', 'Compton', 'Compton', 0]                  # row 5: 222
    PvsA_File.append(row)
    row = ['type 6', 'Compton', 'Compton', 'None Compton', 0]             # row 6: 221, 220
    PvsA_File.append(row)
    row = ['type 7', 'None', 'None', 'Compton', 0]                        # row 7: 002, 012, 102, 022, 202 
    PvsA_File.append(row)
    row = ['type 8', 'None', 'None', 'None Compton', 0]                   # row 8: 000, 001, 010, 011, 100, 101
    PvsA_File.append(row)                                                 #        020, 021, 200, 201
    
    def PA_group(temp):
        ID0, ID1, ID2 = 0, 0, 0
        for j in range(0,len(temp)):
            if j%2==1:
                continue
            elif temp[j]==0:
                if temp[j+1]==0:
                    ID0 = 1
                else:
                    ID0 = 2
            elif temp[j]==1:
                if temp[j+1]==0:
                    ID1 = 1
                else:
                    ID1 = 2
            elif temp[j]==2:
                if temp[j+1]==0:
                    ID2 = 1
                else:
                    ID2 = 2
        if ID1==0 or ID2==0:
            if ID0==2:
                x = 7
            else: 
                x = 8
        elif ID1==2 and ID2==2:
            if ID0==2:
                x = 5
            else:
                x = 6
        elif ID1==1 and ID2==1:
            if ID0==2:
                x = 1
            else:
                x = 2
        else:
            if ID0==2:
                x = 3
            else:
                x = 4
        return(x)
    
#     If the Gamma ID (0, 1, 2) is not present, it is showen by 0
#     If the Gamma ID (0, 1, 2) doesn't have Compton scatter, it is "None Compton" and it is showen by 1
#     If the Gamma ID (0, 1, 2) has Compton scatter, it is "Compton" and it is showen by 2
    for i in range(1, len(CP_Count_File)-1):
        row = CP_Count_File[i]
        row1 = CP_Count_File[i-1]
        if row1[0]==row[0] and row1[1]==row[1]:
            continue
        T = 0
        idx = i + 1
        temp = [] 
        temp.append(row[2]) # The gamme ID of the event 
        temp.append(row[4]) # The number of Comptons in the gamma ID of the event
        while T==0:
            row1 = CP_Count_File[idx]
            if row1[0]==row[0] and row1[1]==row[1] and row1[2]!=row[2]:
                temp.append(row1[2])
                temp.append(row1[4])
            elif row1[0]==row[0] and row1[1]==row[1] and row1[2]==row[2]:
                if row1[4]>0:
                    temp[len(temp)-1] = 2
            else:
                T = 1
            idx = idx + 1 
            if idx>=len(CP_Count_File):
                T = 1
        x = PA_group(temp)
        PvsA_File[x][4] = PvsA_File[x][4] + 1
        total = total + 1
                
    for i in range(1, 9):
        temp = float(PvsA_File[i][4] / total)
        temp = temp * 100
        per = round(temp, 4)
        PvsA_File[i][4] = per
        
    print('Done processing')
    print(f'The number of total events in the Prompt vs Annihilation table is {total} \n',
          f'The Prompt vs Annihilation table is saved as PvsA.csv \n')
        
    print('Reading the Prompt vs Annihilation file into memory...', end='')
    with open(path, mode='w', newline='') as f:
        writer = csv.writer(f)
        for i in PvsA_File:
            writer.writerow(i)
    print('done')
        
    return(PvsA_File)


# In[10]:


# Decide what to do with the Raw Hit File
answer_raw_hit_path           = "n"
answer_output_path            = "n"
answer_Slim_Hit  = "y"
answer_CP_Count  = "y"
answer_CP_Table  = "y"
answer_Coin_Pair = "y"
answer_DCS       = "y"
answer_DCS_Pos   = "y"
answer_PvsA      = "y"

# # The Raw Hit File path
# print("The Raw Hit File is located at: \n")
# print(Raw_Hit_Path)
# print("if you want to change the Raw Hit File path type Y, otherwise type N \n")
# input(answer_raw_hit_path)
# if answer_raw_hit_path == "Y":
#     print("Insert the Raw Hit File path")
#     input(Raw_Hit_Path)
# elif answer_raw_hit_path == "y":
#     print("Insert the Raw Hit File path")
#     input(Raw_Hit_Path)

# # The output path
# print("The output path is located at: \n")
# print(output_path)
# print("if you want to change the output path type Y, otherwise type N \n")
# input(answer_output_path)
# if answer_output_path == "Y":
#     print("Insert the output path")
#     input(output_path)
# elif answer_output_path == "y":
#     print("Insert the output path")
#     input(output_path)
    
# # Generating the Slim Hit File
# print("\n")
# answer_Slim_Hit = input("If you want the Slim Hit type (Y), otherwise type (N) : \n")
# answer_CP_Count = input("If you want the Compton PHotoElectric (CP) Counts type (Y), otherwise type (N) : \n")
# answer_CP_Table = input("If you want the Compron PhotoElectric (CP) Table type (Y), otherwise type (N) : \n")
# answer_Coin_Pair = input("If you want the Coincidence Pairs type (Y), otherwise type (N) : \n")
# answer_DCS = input("If you want the Double Compton Scatter (DCS) events type (Y), otherwise type (N) : \n")
# answer_DCS_Pos = input("If you want the Double Compton Scatter (DCS) Pairs type (Y), otherwise type (N) : \n")
# answer_PvsA = input("If you want the Prompt vs Aniihilation table type (Y), otherwise type (N) : \n")
# print("\n")

print("------------------")
print("\n")
if answer_Slim_Hit=="Y" or answer_CP_Count=="Y" or answer_Coin_Pair=="Y" or answer_DCS_Pos=="Y":
    Slim_Hit_File = Slim_Hit(Raw_Hit_Path)
elif answer_Slim_Hit=="y" or answer_CP_Count=="y" or answer_Coin_Pair=="y" or answer_DCS_Pos=="y":
    Slim_Hit_File = Slim_Hit(Raw_Hit_Path)
    
print("\n")
print("------------------")
print("\n")
if answer_CP_Count=="Y" or answer_CP_Table=="Y" or answer_Coin_Pair=="Y" or answer_DCS=="Y":
    CP_Count_File = CP_Count(Slim_Hit_File)
elif answer_CP_Count=="y" or answer_CP_Table=="y" or answer_Coin_Pair=="y" or answer_DCS=="y":
    CP_Count_File = CP_Count(Slim_Hit_File)

print("\n")
print("------------------")
print("\n")
if answer_CP_Table=="Y":
    CP_Table_File = CP_Table(CP_Count_File)
elif answer_CP_Table=="y":
    CP_Table_File = CP_Table(CP_Count_File)

print("\n")
print("------------------")
print("\n")
if answer_Coin_Pair=="Y":
    Coin_Pair_File = Coin_Pair(Slim_Hit_File, CP_Count_File)
elif answer_Coin_Pair=="y":
    Coin_Pair_File = Coin_Pair(Slim_Hit_File, CP_Count_File)
    
print("\n")
print("------------------")
print("\n")
if answer_DCS=="Y" or answer_DCS_Pos=="Y":
    DCS_File = DCS(CP_Count_File)
elif answer_DCS=="y" or answer_DCS_Pos=="y":
    DCS_File = DCS(CP_Count_File)

print("\n")
print("------------------")
print("\n")
if answer_DCS_Pos=="Y":
    DCS_Pos_File = DCS_Pos(Slim_Hit_File, DCS_File)
elif answer_DCS_Pos=="y":
    DCS_Pos_File = DCS_Pos(Slim_Hit_File, DCS_File)
    
print("\n")
print("------------------")
print("\n")
if answer_PvsA=="Y":
    PvsA_File = PvsA(CP_Count_File)
elif answer_PvsA=="y":
    PvsA_File = PvsA(CP_Count_File)


# In[ ]:




