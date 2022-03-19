#include <iostream>
#include <cmath>
using namespace std ;
int main()
 {
     float a ; float b; float c;float delta;float x1;float x2;
   cout << "ax²+bx+c=0 Equation solver :" << endl;
  cout << "please enter a"<<endl;
  cin >>a;
  cout << "please enter b"<<endl;
  cin >>b;
  cout<<"plese enter c "<<endl;
  cin >>c;
  delta = b*b-4*a*c;
  cout<<"Delta is "<<delta <<endl;
  if (delta<0) {
      cout<<"There is no solution on R" <<endl;
  }
  else if (delta==0) {
      x1=(-b)/(2*a);
      cout <<"x1=x2 and The solution is "<<x1 <<endl;
  }
  else {
      x1=(-b-sqrt(delta))/(2*a);
      x2=(-b+sqrt(delta))/(2*a);
      cout <<"There is two solutions to this equation x1="<<x1 <<" x2="<<x2;
  }
  return 0;
 }
