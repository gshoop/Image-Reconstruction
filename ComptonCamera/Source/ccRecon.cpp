#include <stdio.h>
#include <iostream>
#include <math.h>
#include "../Headers/ccFunctions.h"

using namespace std;

int main(int argc, char const *argv[])
{
    // Need to fix input string path so it cane be used on multiple systems. Currently it seems only absolute paths work.
    string input_path = "/home/swuupie/Image-Reconstruction/CZT_HN/output/dcs.dat";
    // Need to define the FOV (or source space) and voxelize
    float x_begin, x_end, y_begin, y_end, z_begin, z_end;
    unsigned numVox_x, numVox_y, numVox_z;
    long unsigned cone_count;

    x_begin = -100.0; x_end = 100.0;
    y_begin = -75.0; y_end = 75.0;
    z_begin = -100.0; z_end = 100.0;
    numVox_x = 40; numVox_z = 40; numVox_y = 30;

    // Voxel dimensions
    const float delx = (x_end - x_begin)/numVox_x;
    const float dely = (y_end - y_begin)/numVox_y;
    const float delz = (z_end - z_begin)/numVox_z;

    cout << "Voxel dimensions: " << delx << "," << dely << "," << delz << "\n" << endl;

    // Instantiating the voxel position matrix and source distribution vector
    vector<vector<vector<vector<float> > > > position_matrix(numVox_x, vector<vector<vector<float> > >(numVox_y, vector<vector<float> >(numVox_z , {0,0,0} ) ) );
    float* f = new float [numVox_x*numVox_y*numVox_z]{};

    // Fills position_matrix with coordinates representing the center of the voxels in the FOV
    DefinePostionMatrix(position_matrix, f, numVox_x, numVox_y, numVox_z, x_begin, y_begin, z_begin, delx, dely, delz);
    cone_count = CountCones(input_path);

    float* conelist_1D = new float[cone_count * 9]{};

    ConstructCones(conelist_1D, input_path, cone_count);

    return 0;
}
