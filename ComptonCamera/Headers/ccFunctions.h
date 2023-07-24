#include <iostream>
#include <fstream>
#include <stdio.h>
#include <vector>
#include <stdlib.h>
#include <math.h>
#include <string>
#include <sstream>

using namespace std;

void DefinePostionMatrix( vector<vector<vector<vector<float> > > > &pos_matrix, float* f, unsigned x_vox, unsigned y_vox, unsigned z_vox,
                          float x_start, float y_start, float z_start, float delx, float dely, float delz );

void ConstructCones( float* conelist_1D, string input, long unsigned num_cones);

vector<float> ScalarVec(float c, vector<float> x);

vector<float> UnitVector(vector<float> start, vector<float> end);

long unsigned CountCones(string input);

float PolarScatteringAngle(float E1, float E2);