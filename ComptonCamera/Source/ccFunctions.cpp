#include "../Headers/ccFunctions.h"
#include <iostream>

using namespace std;

void DefinePostionMatrix( vector<vector<vector<vector<float> > > > &pos_matrix, float* f, unsigned x_vox, unsigned y_vox, unsigned z_vox,
                          float x_start, float y_start, float z_start, float delx, float dely, float delz ){

    cout << "Defining Position Matrix...." << "\n" << endl;

    for (unsigned i = 0; i < x_vox; i++) {
        for (unsigned j = 0; j < y_vox; j++) {
            for (unsigned k = 0; k < z_vox; k++) {
                pos_matrix[i][j][k] = { x_start + delx * (float)(i + 0.5), y_start + dely * (float)(j + 0.5), z_start + delz * (float)(k + 0.5) };

                f[ i + j * x_vox + k * x_vox * y_vox] = 1.0;

                // *********************************************
                // FOR DEBUGING PURPOSES
                // *********************************************
                // Print out the position of center of each voxel.
                // for (int l = 0; l < 3; l++) {
                //     if (l == 0) {
                //         cout << "{ ";
                //     }
                //     cout << pos_matrix[i][j][k][l] << " ";
                //     if (l == 2) {
                //         cout << "}, ";
                //     }
                // }
            }
        }
    }
    cout << "Position Matrix complete..." << "\n" << endl;
}

void ConstructCones( float* conelist_1D, string input){
    cout << "Reading input data and constructing cones list..." << "\n" << endl;

    ifstream file ( input );
    vector<float> linledata;
    string line;
    float E1, E2;
    float theta, utheta, KN;
    unsigned errors = 0;

    // Count rows of input file for total number of compton cones
    unsigned count = 0;
    while (getline(file, line)) {
        count++;
    }
    cout << "There are a total of " << count << " compton cones.\n" << endl;
}