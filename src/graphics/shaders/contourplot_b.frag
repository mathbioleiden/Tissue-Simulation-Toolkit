#version 430 core
in vec4 gl_FragCoord;
out vec4 color;
layout (location = 2) uniform vec3 size;
layout (location = 6) uniform vec2 windowSize;
layout (location = 9) uniform float l_width;

in Data {
  vec4 col;
} cin;

layout (std430, binding=5) buffer density{
  float dense[];
};


  vec2 point0;
  bool ul_h = false;
  bool um_h = false;
  bool ur_h = false;
  bool ml_h = false;
  bool mm_h = false;
  bool mr_h = false;
  bool dl_h = false;
  bool dm_h = false;
  bool dr_h = false;
  float ul = 0;
  float um = 0;
  float ur = 0;
  float ml = 0; 
  float mm = 0;
  float mr = 0;
  float dl = 0;
  float dm = 0;
  float dr = 0;


void line(vec2 point1, vec2 point2) {
  float distance = abs(((point2.x - point1.x) * (point1.y - point0.y) - 
  (point1.x - point0.x)*(point2.y - point1.y)) /
  sqrt((pow((point2.x - point1.x),2) + pow((point2.y - point1.y), 2))));
  if (distance < l_width &&
      point0.x > min(point1.x, point2.x) - l_width &&
      point0.x < max(point1.x, point2.x) + l_width &&
      point0.y > min(point1.y, point2.y) - l_width &&
      point0.y < max(point1.y, point2.y) + l_width) {
  color.a = 1;
  }
}


void make_profile(float mm_f) {
  ul_h = ul > mm_f;
  um_h = um > mm_f;
  ur_h = ur > mm_f;
  ml_h = ml > mm_f;
  mm_h = mm > mm_f;
  mr_h = mr > mm_f;
  dl_h = dl > mm_f;
  dm_h = dm > mm_f;
  dr_h = dr > mm_f;
}


float inb(vec2 p1, vec2 p2, float y) {
  float f = (p2.y - p1.y) * (p2.x - p1.x);
  float a = p1.y - p1.x * f;
  float x = (y - a) / f;
  return x;
}


void main(){
  vec2 pos = gl_FragCoord.xy / windowSize.xy * size.xy;
  float fx = pos.x ;
  float fy = pos.y ;
  int x = int(fx);
  int y = int(fy);
  float ix = fx - float(x); 
  float iy = fy - float(y);
  int sx = int(size.x);
  int sy = int(size.y);
  point0 = vec2(ix, iy); 
  mm = dense[x*int(size.y)+y];

  if (x != 0 && y != 0) dl = dense[(x-1)*sy+(y-1)];
  if (y != 0) dm = dense[(x)*sy+(y-1)];
  if (x < sx && y != 0) dr = dense[(x+1)*sy+(y-1)];
  if (x != 0) ml = dense[(x-1)*sy+(y)];
  if (x < sx) mr = dense[(x+1)*sy+(y)];
  if (x != 0 && y < sy) ul = dense[(x-1)*sy+(y+1)];
  if (y < sy) um = dense[(x)*sy+(y+1)];
  if (y < sy) ur = dense[(x+1)*sy+(y+1)];
  
  color = cin.col; 
  color.a = 0;
  int res = 0;
  
  int start = int(mm) - 1; 
  for (float mm_f = float(start); mm_f < start + 3;  mm_f++){
    make_profile(mm_f);
    if (mm != ul || mm != um || mm != ur || mm != ml || mm != mr || mm != dl || mm != dm || mm != dr){
      //Diagonal Left Down 
      if (ml_h && !mm_h && dl_h && dm_h || !ml_h && mm_h && !dl_h && !dm_h ) {
        line(vec2(0.5,0.0), vec2(0.0,0.5));
      } 
      //Diagonal Left Up
      if (ul_h && um_h && ml_h && !mm_h || !ul_h && !um_h && !ml_h && mm_h ) {
        line(vec2(0.0,0.5), vec2(0.5,1.0));
      }
      //Diagonal Right Down
      if (!mm_h && mr_h && dm_h && dr_h || mm_h && !mr_h && !dm_h && !dr_h ) {
        line(vec2(0.5,0.0), vec2(1.0,0.5));
      }
      //Diagonal Right Up
      if (um_h && ur_h && !mm_h && mr_h || !um_h && !ur_h && mm_h && !mr_h ) {
        line(vec2(1.0,0.5), vec2(0.5,1.0));
      }
      if (ul_h && !um_h && ml_h && !mm_h || !ul_h && um_h && !ml_h && mm_h ) {
        line(vec2(0.0,0.5), vec2(0.0,1.0));
      }
      //Vertical Left Down
      if (ml_h && !mm_h && dl_h && !dm_h || !ml_h && mm_h && !dl_h && dm_h ) {
        line(vec2(0.0,0.0), vec2(0.0,0.5));
      }
      //Vertical Right Up
      if (um_h && !ur_h && mm_h && !mr_h || !um_h && ur_h && !mm_h && mr_h) {
        line(vec2(1.0,0.5), vec2(1.0,1.0)); 
      }
      //Vertical Right down
      if (mm_h && !mr_h && dm_h && !dr_h ||  !mm_h && mr_h && !dm_h && dr_h) {
        line(vec2(1.0,0.0), vec2(1.0,0.5));
      }
      //Horizontal Down Left
      if (ml_h && mm_h && !dl_h && !dm_h || !ml_h && !mm_h && dl_h && dm_h) {
        line(vec2(0.0,0.0), vec2(0.5,0.0));
      }
      //Horizontal Down Right
      if (mm_h && mr_h && !dm_h && !dr_h || !mm_h && !mr_h && dm_h && dr_h)  {
        line(vec2(0.5,0.0), vec2(1.0,0.0));
      }
      //Horizontal Up Left  
      if (ul_h && um_h && !ml_h && !mm_h || !ul_h && !um_h && ml_h && mm_h)  {
        line(vec2(0.0,1.0), vec2(0.5,1.0));
      }
      //Horizontal Up Right 
      if (um_h && ur_h && !mm_h && !mr_h || !um_h && !ur_h && mm_h && mr_h)  {
        line(vec2(0.5,1.0), vec2(1.0,1.0));
      }
    }
  }
}
