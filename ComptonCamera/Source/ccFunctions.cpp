#include "ccFunctions.h"

void DefinePostionMatrix( vector<vector<vector<vector<float> > > > &pos_matrix, float* f, unsigned x_vox, unsigned y_vox, unsigned z_vox,
                          float x_start, float y_start, float z_start, float delx, float dely, float delz ){

    cout << "Defining Position Matrix...." << "\n" << endl;

    for (unsigned i = 0; i < x_vox; i++) {
        for (unsigned j = 0; j < y_vox; j++) {
            for (unsigned k = 0; k < z_vox; k++) {

                pos_matrix[i][j][k] = { x_start + delx * (float)(i + 0.5), y_start + dely * (float)(j + 0.5), z_start + delz * (float)(k + 0.5) };

                f[ i + j * x_vox + k * x_vox * y_vox] = 1.0;
            }
        }
    }

    cout << "Position Matrix complete..." << "\n" << endl;

}