#include <iostream>
#include <stdio.h>
#include <vector>
#include <stdlib.h>
#include <math.h>

using namespace std;

void DefinePostionMatrix( vector<vector<vector<vector<float> > > > &pos_matrix, float* f, unsigned x_vox, unsigned y_vox, unsigned z_vox,
                          float x_start, float y_start, float z_start, float delx, float dely, float delz );

void ConstructCones( float* conelist_1D, string input);