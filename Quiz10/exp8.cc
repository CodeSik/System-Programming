#include <cstdlib>			// for free()

int main() {
    double *p =(double*)malloc(sizeof(double)*1000); 
    free(p);
    return 0;
}
