#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <cmath>
#include <cstdlib>
#include "time.h"
using namespace std;


ofstream ofile;

//setting up needed functions before main function
// func is the second-derivative of u(x)
// exact is the analytical solution
// rel_err calculates log10 of the relative error
double func(double x){return 100.0*exp(-10.0*x);} // Second derivative of function

double exact(double x){return 1.0-(1-exp(-10))*x-exp(-10*x);} // Function

double rel_err(double x, double y) {return log10(abs(y-x)/x);}

int main(int argc, char *argv[])
{
    int exponent;
      string filename;
      if( argc <=2 ){
          cout << "Bad usage: " << argv[0] <<
                  " read also file name on same line and max power of 10^n" << endl;
          exit(1);
      }
      else{
        filename = argv[1];
        exponent = atoi(argv[2]);
      }
      int n = (int) pow(10.0, exponent);
      string fileout = filename;
      // Setting up the arrays needed for solving the general
      // case of the Thomas algorithm. (Memory allocation)
      double h = 1.0/(n);
      double hh = h*h;
      double *d, *g, *u, *x, *xact;
      d = new double[n];
      g = new double[n];
      u = new double[n];
      x = new double[n];
      xact = new double[n];
      u[0] = double(0.0);
      u[n-1] = double(0.0);
      // Timing the functions
      clock_t start, finish;
      for (int i=0; i<n; i++) {
          d[i] = double(2.0-i/(i+1)); //precalculating tilde(d)
          g[i] = double(hh*func(i*h));
          x[i] = double(i*h);
          xact[i] = double(exact(i*h));
      }
      start = clock();
      //Forward substitution
      //Note that d is precalculated and is not in
      // the for-loop below.
      for (int i=1; i<n-1; i++) {
          g[i] = g[i]+g[i-1]/d[i-1]; // Calculating b as in the report (Theory, the Thomas algorithm, Specifics of the case, expression 11)
      }
      //Backward substitution
      u[n-2] = g[n-2]/d[n-2]; // Finding v_(n-1) as in the report (Theory, The Thomas Algorithm, Backwards substitution)
      for (int i=0; i<n-3; i++) {
          u[n-3-i] = (g[n-3-i]+u[n-2-i])/d[n-3-i]; // Calculating v as in the report (Theory, the Thomas algorithm, Specifics of the case, expression 12)
      }
      // End of function, hereby stopping the timer
      finish = clock();
      // Opening file to write out results to
      ofile.open(fileout);
      for (int i=0; i<n; i++) {
          string argument = to_string(i);
          fileout.append(argument);
          ofile << setiosflags(ios::showpoint | ios::uppercase) << setw(20)<<setprecision(8)<< x[i] << "," << setw(20) << setprecision(8)<< scientific << u[i] << "," << setw(20) << rel_err(xact[i],u[i]) << endl;
      }
      ofile.close();
      // Finding maximum of relative error
      double max_value = 0.0;
      double temp;
      for (int i=1; i<n-1; i++){
           temp = rel_err(xact[i],u[i]);
           if(temp*temp>max_value*max_value){max_value = temp;}
      }
      // writing out the timing of the function to the console
      double timeused = (double) (finish-start)/(CLOCKS_PER_SEC );
      cout << setprecision(15) << setw(15) << timeused << endl;
      // writing out maximum value of relative error to the console
      cout << setprecision(15) << max_value << endl;
      // deleting arrays after they have performed their calculations
      // to preserve space (Memory deallocation)
      for (int i=0; i< n; i++) {
          delete[] d;
          delete[] g;
          delete[] u;
          delete[] x;
          delete[] xact;
      }
}
