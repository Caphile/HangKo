#include <iostream>
using namespace std; //

class Circle
{
public:
  int radius;
  double getArea();
};

double Circle::getArea()
{
  return 3.14 * radius * radius;      //
}

int main()
{
  Circle donut;
  donut.radius = 1;
  double area = donut.getArea();
  cout << "donut 면적은" << area << endl;

  Circle pizza;
  pizza.radius = 30;
  area = pizza.getArea();
  cout << "pizza 면적은" << area << endl;
}

int main()
{
  Rectangle rect;
  rect.width = 3;
  rect.height = 5;
  cout << "사각형의 면적은 " << rect.getArea() << endl;
}
