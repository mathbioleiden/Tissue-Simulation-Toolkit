// Class point needed by 2D convex hull code
class Point {

public:
  Point(float xx, float yy) {
    x=xx;
    y=yy;
  }
  Point(void) {
    x=0; y=0;
  }
  float x,y;

};

int chainHull_2D( Point* P, int n, Point* H );

