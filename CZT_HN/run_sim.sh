#!/bin/bash
(
(
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_0 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_1 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_2 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_3 &
wait
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_0][timeslice,1.0][timestart,0.0][timestop,1.0] main.mac > ./log/log_0.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_1][timeslice,1.0][timestart,1.0][timestop,2.0] main.mac > ./log/log_1.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_2][timeslice,1.0][timestart,2.0][timestop,3.0] main.mac > ./log/log_2.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_3][timeslice,1.0][timestart,3.0][timestop,4.0] main.mac > ./log/log_3.txt &
wait
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_4 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_5 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_6 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_7 &
wait
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_4][timeslice,1.0][timestart,4.0][timestop,5.0] main.mac > ./log/log_4.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_5][timeslice,1.0][timestart,5.0][timestop,6.0] main.mac > ./log/log_5.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_6][timeslice,1.0][timestart,6.0][timestop,7.0] main.mac > ./log/log_6.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_7][timeslice,1.0][timestart,7.0][timestop,8.0] main.mac > ./log/log_7.txt &
wait
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_8 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_9 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_10 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_11 &
wait
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_8][timeslice,1.0][timestart,8.0][timestop,9.0] main.mac > ./log/log_8.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_9][timeslice,1.0][timestart,9.0][timestop,10.0] main.mac > ./log/log_9.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_10][timeslice,1.0][timestart,10.0][timestop,11.0] main.mac > ./log/log_10.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_11][timeslice,1.0][timestart,11.0][timestop,12.0] main.mac > ./log/log_11.txt &
wait
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_12 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_13 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_14 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_15 &
wait
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_12][timeslice,1.0][timestart,12.0][timestop,13.0] main.mac > ./log/log_12.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_13][timeslice,1.0][timestart,13.0][timestop,14.0] main.mac > ./log/log_13.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_14][timeslice,1.0][timestart,14.0][timestop,15.0] main.mac > ./log/log_14.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_15][timeslice,1.0][timestart,15.0][timestop,16.0] main.mac > ./log/log_15.txt &
wait
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_16 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_17 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_18 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_19 &
wait
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_16][timeslice,1.0][timestart,16.0][timestop,17.0] main.mac > ./log/log_16.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_17][timeslice,1.0][timestart,17.0][timestop,18.0] main.mac > ./log/log_17.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_18][timeslice,1.0][timestart,18.0][timestop,19.0] main.mac > ./log/log_18.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_19][timeslice,1.0][timestart,19.0][timestop,20.0] main.mac > ./log/log_19.txt &
wait
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_20 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_21 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_22 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_23 &
wait
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_20][timeslice,1.0][timestart,20.0][timestop,21.0] main.mac > ./log/log_20.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_21][timeslice,1.0][timestart,21.0][timestop,22.0] main.mac > ./log/log_21.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_22][timeslice,1.0][timestart,22.0][timestop,23.0] main.mac > ./log/log_22.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_23][timeslice,1.0][timestart,23.0][timestop,24.0] main.mac > ./log/log_23.txt &
wait
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_24 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_25 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_26 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_27 &
wait
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_24][timeslice,1.0][timestart,24.0][timestop,25.0] main.mac > ./log/log_24.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_25][timeslice,1.0][timestart,25.0][timestop,26.0] main.mac > ./log/log_25.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_26][timeslice,1.0][timestart,26.0][timestop,27.0] main.mac > ./log/log_26.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_27][timeslice,1.0][timestart,27.0][timestop,28.0] main.mac > ./log/log_27.txt &
wait
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_28 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_29 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_30 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_31 &
wait
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_28][timeslice,1.0][timestart,28.0][timestop,29.0] main.mac > ./log/log_28.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_29][timeslice,1.0][timestart,29.0][timestop,30.0] main.mac > ./log/log_29.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_30][timeslice,1.0][timestart,30.0][timestop,31.0] main.mac > ./log/log_30.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_31][timeslice,1.0][timestart,31.0][timestop,32.0] main.mac > ./log/log_31.txt &
wait
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_32 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_33 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_34 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_35 &
wait
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_32][timeslice,1.0][timestart,32.0][timestop,33.0] main.mac > ./log/log_32.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_33][timeslice,1.0][timestart,33.0][timestop,34.0] main.mac > ./log/log_33.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_34][timeslice,1.0][timestart,34.0][timestop,35.0] main.mac > ./log/log_34.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_35][timeslice,1.0][timestart,35.0][timestop,36.0] main.mac > ./log/log_35.txt &
wait
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_36 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_37 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_38 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_39 &
wait
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_36][timeslice,1.0][timestart,36.0][timestop,37.0] main.mac > ./log/log_36.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_37][timeslice,1.0][timestart,37.0][timestop,38.0] main.mac > ./log/log_37.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_38][timeslice,1.0][timestart,38.0][timestop,39.0] main.mac > ./log/log_38.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_39][timeslice,1.0][timestart,39.0][timestop,40.0] main.mac > ./log/log_39.txt &
wait
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_40 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_41 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_42 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_43 &
wait
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_40][timeslice,1.0][timestart,40.0][timestop,41.0] main.mac > ./log/log_40.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_41][timeslice,1.0][timestart,41.0][timestop,42.0] main.mac > ./log/log_41.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_42][timeslice,1.0][timestart,42.0][timestop,43.0] main.mac > ./log/log_42.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_43][timeslice,1.0][timestart,43.0][timestop,44.0] main.mac > ./log/log_43.txt &
wait
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_44 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_45 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_46 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_47 &
wait
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_44][timeslice,1.0][timestart,44.0][timestop,45.0] main.mac > ./log/log_44.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_45][timeslice,1.0][timestart,45.0][timestop,46.0] main.mac > ./log/log_45.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_46][timeslice,1.0][timestart,46.0][timestop,47.0] main.mac > ./log/log_46.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_47][timeslice,1.0][timestart,47.0][timestop,48.0] main.mac > ./log/log_47.txt &
wait
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_48 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_49 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_50 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_51 &
wait
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_48][timeslice,1.0][timestart,48.0][timestop,49.0] main.mac > ./log/log_48.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_49][timeslice,1.0][timestart,49.0][timestop,50.0] main.mac > ./log/log_49.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_50][timeslice,1.0][timestart,50.0][timestop,51.0] main.mac > ./log/log_50.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_51][timeslice,1.0][timestart,51.0][timestop,52.0] main.mac > ./log/log_51.txt &
wait
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_52 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_53 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_54 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_55 &
wait
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_52][timeslice,1.0][timestart,52.0][timestop,53.0] main.mac > ./log/log_52.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_53][timeslice,1.0][timestart,53.0][timestop,54.0] main.mac > ./log/log_53.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_54][timeslice,1.0][timestart,54.0][timestop,55.0] main.mac > ./log/log_54.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_55][timeslice,1.0][timestart,55.0][timestop,56.0] main.mac > ./log/log_55.txt &
wait
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_56 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_57 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_58 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_59 &
wait
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_56][timeslice,1.0][timestart,56.0][timestop,57.0] main.mac > ./log/log_56.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_57][timeslice,1.0][timestart,57.0][timestop,58.0] main.mac > ./log/log_57.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_58][timeslice,1.0][timestart,58.0][timestop,59.0] main.mac > ./log/log_58.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_59][timeslice,1.0][timestart,59.0][timestop,60.0] main.mac > ./log/log_59.txt &
wait
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_60 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_61 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_62 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_63 &
wait
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_60][timeslice,1.0][timestart,60.0][timestop,61.0] main.mac > ./log/log_60.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_61][timeslice,1.0][timestart,61.0][timestop,62.0] main.mac > ./log/log_61.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_62][timeslice,1.0][timestart,62.0][timestop,63.0] main.mac > ./log/log_62.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_63][timeslice,1.0][timestart,63.0][timestop,64.0] main.mac > ./log/log_63.txt &
wait
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_64 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_65 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_66 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_67 &
wait
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_64][timeslice,1.0][timestart,64.0][timestop,65.0] main.mac > ./log/log_64.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_65][timeslice,1.0][timestart,65.0][timestop,66.0] main.mac > ./log/log_65.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_66][timeslice,1.0][timestart,66.0][timestop,67.0] main.mac > ./log/log_66.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_67][timeslice,1.0][timestart,67.0][timestop,68.0] main.mac > ./log/log_67.txt &
wait
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_68 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_69 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_70 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_71 &
wait
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_68][timeslice,1.0][timestart,68.0][timestop,69.0] main.mac > ./log/log_68.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_69][timeslice,1.0][timestart,69.0][timestop,70.0] main.mac > ./log/log_69.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_70][timeslice,1.0][timestart,70.0][timestop,71.0] main.mac > ./log/log_70.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_71][timeslice,1.0][timestart,71.0][timestop,72.0] main.mac > ./log/log_71.txt &
wait
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_72 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_73 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_74 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_75 &
wait
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_72][timeslice,1.0][timestart,72.0][timestop,73.0] main.mac > ./log/log_72.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_73][timeslice,1.0][timestart,73.0][timestop,74.0] main.mac > ./log/log_73.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_74][timeslice,1.0][timestart,74.0][timestop,75.0] main.mac > ./log/log_74.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_75][timeslice,1.0][timestart,75.0][timestop,76.0] main.mac > ./log/log_75.txt &
wait
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_76 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_77 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_78 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_79 &
wait
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_76][timeslice,1.0][timestart,76.0][timestop,77.0] main.mac > ./log/log_76.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_77][timeslice,1.0][timestart,77.0][timestop,78.0] main.mac > ./log/log_77.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_78][timeslice,1.0][timestart,78.0][timestop,79.0] main.mac > ./log/log_78.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_79][timeslice,1.0][timestart,79.0][timestop,80.0] main.mac > ./log/log_79.txt &
wait
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_80 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_81 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_82 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_83 &
wait
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_80][timeslice,1.0][timestart,80.0][timestop,81.0] main.mac > ./log/log_80.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_81][timeslice,1.0][timestart,81.0][timestop,82.0] main.mac > ./log/log_81.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_82][timeslice,1.0][timestart,82.0][timestop,83.0] main.mac > ./log/log_82.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_83][timeslice,1.0][timestart,83.0][timestop,84.0] main.mac > ./log/log_83.txt &
wait
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_84 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_85 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_86 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_87 &
wait
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_84][timeslice,1.0][timestart,84.0][timestop,85.0] main.mac > ./log/log_84.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_85][timeslice,1.0][timestart,85.0][timestop,86.0] main.mac > ./log/log_85.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_86][timeslice,1.0][timestart,86.0][timestop,87.0] main.mac > ./log/log_86.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_87][timeslice,1.0][timestart,87.0][timestop,88.0] main.mac > ./log/log_87.txt &
wait
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_88 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_89 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_90 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_91 &
wait
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_88][timeslice,1.0][timestart,88.0][timestop,89.0] main.mac > ./log/log_88.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_89][timeslice,1.0][timestart,89.0][timestop,90.0] main.mac > ./log/log_89.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_90][timeslice,1.0][timestart,90.0][timestop,91.0] main.mac > ./log/log_90.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_91][timeslice,1.0][timestart,91.0][timestop,92.0] main.mac > ./log/log_91.txt &
wait
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_92 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_93 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_94 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_95 &
wait
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_92][timeslice,1.0][timestart,92.0][timestop,93.0] main.mac > ./log/log_92.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_93][timeslice,1.0][timestart,93.0][timestop,94.0] main.mac > ./log/log_93.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_94][timeslice,1.0][timestart,94.0][timestop,95.0] main.mac > ./log/log_94.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_95][timeslice,1.0][timestart,95.0][timestop,96.0] main.mac > ./log/log_95.txt &
wait
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_96 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_97 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_98 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_99 &
wait
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_96][timeslice,1.0][timestart,96.0][timestop,97.0] main.mac > ./log/log_96.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_97][timeslice,1.0][timestart,97.0][timestop,98.0] main.mac > ./log/log_97.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_98][timeslice,1.0][timestart,98.0][timestop,99.0] main.mac > ./log/log_98.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_99][timeslice,1.0][timestart,99.0][timestop,100.0] main.mac > ./log/log_99.txt &
wait
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_100 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_101 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_102 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_103 &
wait
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_100][timeslice,1.0][timestart,100.0][timestop,101.0] main.mac > ./log/log_100.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_101][timeslice,1.0][timestart,101.0][timestop,102.0] main.mac > ./log/log_101.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_102][timeslice,1.0][timestart,102.0][timestop,103.0] main.mac > ./log/log_102.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_103][timeslice,1.0][timestart,103.0][timestop,104.0] main.mac > ./log/log_103.txt &
wait
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_104 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_105 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_106 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_107 &
wait
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_104][timeslice,1.0][timestart,104.0][timestop,105.0] main.mac > ./log/log_104.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_105][timeslice,1.0][timestart,105.0][timestop,106.0] main.mac > ./log/log_105.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_106][timeslice,1.0][timestart,106.0][timestop,107.0] main.mac > ./log/log_106.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_107][timeslice,1.0][timestart,107.0][timestop,108.0] main.mac > ./log/log_107.txt &
wait
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_108 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_109 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_110 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_111 &
wait
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_108][timeslice,1.0][timestart,108.0][timestop,109.0] main.mac > ./log/log_108.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_109][timeslice,1.0][timestart,109.0][timestop,110.0] main.mac > ./log/log_109.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_110][timeslice,1.0][timestart,110.0][timestop,111.0] main.mac > ./log/log_110.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_111][timeslice,1.0][timestart,111.0][timestop,112.0] main.mac > ./log/log_111.txt &
wait
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_112 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_113 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_114 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_115 &
wait
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_112][timeslice,1.0][timestart,112.0][timestop,113.0] main.mac > ./log/log_112.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_113][timeslice,1.0][timestart,113.0][timestop,114.0] main.mac > ./log/log_113.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_114][timeslice,1.0][timestart,114.0][timestop,115.0] main.mac > ./log/log_114.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_115][timeslice,1.0][timestart,115.0][timestop,116.0] main.mac > ./log/log_115.txt &
wait
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_116 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_117 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_118 &
mkdir /mnt/d/HitsGATE/Sc442Ps_output/out_119 &
wait
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_116][timeslice,1.0][timestart,116.0][timestop,117.0] main.mac > ./log/log_116.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_117][timeslice,1.0][timestart,117.0][timestop,118.0] main.mac > ./log/log_117.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_118][timeslice,1.0][timestart,118.0][timestop,119.0] main.mac > ./log/log_118.txt &
Gate -a [outputfolder,/mnt/d/HitsGATE/Sc442Ps_output/out_119][timeslice,1.0][timestart,119.0][timestop,120.0] main.mac > ./log/log_119.txt &
wait
wait
wait
)
) &
htop
