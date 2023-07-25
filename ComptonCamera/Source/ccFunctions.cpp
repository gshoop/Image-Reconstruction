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

void ConstructCones( float* conelist_1D, string input, long unsigned num_cones){
    cout << "Reading input data and constructing cones list..." << "\n" << endl;

    ifstream file ( input );
    vector<float> linedata;
    string line;
    float E1, E2;
    float theta, utheta, KN;
    unsigned errors = 0;

    for (unsigned i = 0; i < num_cones; i++) {

        getline (file, line, '\n');
        stringstream sep(line);
        string cell;

        while (getline (sep, cell, ' ')) {
            linedata.push_back( atof(cell.c_str()) );
        }

        //E1 = linedata[0];
        E1 = linedata[0];
        E2 = linedata[4];

        // Need to compute scattering angle from E1, E2, uncertainty, and klein nishna
        theta = PolarScatteringAngle(E1,E2);


        cout << i << ": Theta value: " << theta << endl;

        if ( theta == 0 ){
            errors++;
            KN = 0;
        }

        // Computing unit vector for cone axis of data. Need to validate DCSc data, some coincidences are scattering to opposite panels.
        vector<float> axis = UnitVector({linedata[5], linedata[6], linedata[7]}, {linedata[1], linedata[2], linedata[3]});

        cout << "Unit Vector: {";
        for (unsigned i = 0; i < axis.size(); i++) {
            if (i < axis.size()-1) {
                cout << axis[i] << ", ";
            } else {
                cout << axis[i] << "}" << endl;
            }
        }

        linedata.clear();
    }

}

vector<float> ScalarVec(float c, vector<float> x){
    unsigned len = x.size();
    vector<float> z(len);

    for (unsigned i = 0; i < len; i++) {
        z[i] = x[i]*c;
    }
    return z;
}

vector<float> UnitVector(vector<float> start, vector<float> end){
    unsigned d = start.size();
    float normsq = 0;
    vector<float> vec(d);

    cout << "Vector: {";
    for (unsigned i = 0; i < d; i++) {
        vec[i] = end[i] - start[i];
        normsq += vec[i] * vec[i];
        if (i < d-1) {
            cout << vec[i] << ", ";
        } else {
            cout << vec[i] << "} ";
        }
    }
    return ScalarVec( 1.0/sqrt(normsq), vec);
}

long unsigned CountCones(string input){
    ifstream file ( input );
    string line;
    unsigned count = 0;

    while (getline(file, line)) {
        count++;
    }
    cout << "There are a total of " << count << " compton cones.\n" << endl;
    return count;
}

float PolarScatteringAngle(float E1, float E2){
    float MCsq = 0.5109989461;
    float value = 1.0 + MCsq * (1.0/(E1 + E2) - 1.0/(E2));
    
    if ( fabs(value) < 1) {
        return acos(value);
    }

    return 0;
}