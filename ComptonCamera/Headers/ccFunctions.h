#include <iostream>
#include <fstream>
#include <stdio.h>
#include <vector>
#include <stdlib.h>
#include <math.h>
#include <string>
#include <sstream>

using namespace std;

//#define DEBUG

void DefinePostionMatrix( vector<vector<vector<vector<float> > > > &pos_matrix, float* f, unsigned x_vox, unsigned y_vox, unsigned z_vox,
                          float x_start, float y_start, float z_start, float delx, float dely, float delz );

void ConstructCones( float* conelist_1D, string input, long unsigned num_cones);

vector<float> ScalarVec(float c, vector<float> x);

vector<float> UnitVector(vector<float> start, vector<float> end);

long unsigned CountCones(string input);

float PolarScatteringAngle(float E1, float E2);

float UncertaintyDoubleScatter(float E1, float E2, float UE);

float KleinNishina(float E1, float E2);

void Find_Intersecting(float *conelist_1D_d, unsigned char *voxel_cone_interaction_d, unsigned x_vox, unsigned y_vox, unsigned z_vox, long unsigned num_cones,
                        float delx, float dely, float delz, float x_start, float y_start, float z_start, unsigned INTSTEP);