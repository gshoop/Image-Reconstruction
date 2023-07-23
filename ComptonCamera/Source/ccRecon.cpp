#include <stdio.h>
#include <iostream>
#include <math.h>

using namespace std;

int main(int argc, char const *argv[])
{
    // Need to define the FOV (or source space) and voxelize
    float x_begin, x_end, y_begin, y_end, z_begin, z_end;
    unsigned numVox_x, numVox_y, numVox_z;

    x_begin = -100.0; x_end = 100.0;
    y_begin = -75.0; y_end = 75.0;
    z_begin = -100.0; z_end = 100.0;
    numVox_x = 40; numVox_z = 40; numVox_y = 30;

    // Voxel dimensions
    const float delx = (x_end - x_begin)/numVox_x;
    const float dely = (y_end - y_begin)/numVox_y;
    const float delz = (z_end - z_begin)/numVox_z;

    cout << "Voxel dimensions: " << delx << "," << dely << "," << delz << "\n" << endl;

    return 0;
}
