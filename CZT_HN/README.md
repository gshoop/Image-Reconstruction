# System Geometry
Below is the geometry of the CZT Dual Panel system. The system is made up of 4 x 4 x 0.5 cm<sup>3</sup> cadmium zinc telluride (CZT) crystals.
![gate2panelrev](https://github.com/gshoop/Image-Reconstruction/assets/44107373/4161e4f0-3089-403c-bbbd-1e59eac27bb5)
Each panel consists 5 columns of 30 CZT crystals stacked on top of one another. The crystals are oriented in an edge-on configuration which allows for 4 cm of CZT thickness in the panel. The area of the panel face is 15 x 20 cm<sup>2</sup> while the distance between the panels is 20 cm.

# Output
Contains GATE simulation output files and scripts.

__partial_Hits.dat__: Raw GATE hit file containing all true information of hits recorded within the detector.

__partial\_.root__: Raw GATE hit file in root file viewing format.

__partial_Run.dat__: Contains the number of events in the run.

__stat.txt__: Contains information about the run.

__slim_hit.dat__: output of dcs_hit.py which removes hits that aren't compton or photoelectric absorption events.

__dcs_hit.dat__: ascii output of dcs_hit.py which contains events in slim_hit.dat that are part of DCSc chains.

__dcs.dat__: Coincidence file containing DCSc event pairs.

__dcs_hit.py__: Script that filters and outputs a dcs.dat file containing coincidences for image reconstruction.
## dcs_hit.py
This file is used to take a raw hit file from the GATE simulation and output an ascii file with the double compton scattering coincidences.