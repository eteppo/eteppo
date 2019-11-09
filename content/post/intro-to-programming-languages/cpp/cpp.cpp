// include iostream (cout) declarations here
// actual code exists in std library
#include <iostream>
// allow writing cout instead of str::cout
using namespace std;
// define class
class Car {
  // declare attributes; data types always needed, values not
  // public means accessible outside class
  public:
    string brand;   
    string model;
    int year;
};
// main function is always run
// returned data type must be declared
int main() {
  // declare new objects of class Car
  // set values to attributes
  Car car1;
  car1.brand = "BMW";
  car1.model = "X5";
  car1.year = 1999;
  Car car2;
  car2.brand = "Ford";
  car2.model = "Mustang";
  car2.year = 1969;
  // c++ way to print to console
  std::cout << car1.brand << " " << car1.model << " " << car1.year << "\n";
  std::cout << car2.brand << " " << car2.model << " " << car2.year << "\n";
  // return nothing (zero)
  return 0;
}
// compile with g++ command line utility
// run compiled program as ./program
