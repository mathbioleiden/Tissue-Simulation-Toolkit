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

float inb(float x1, float y1, float x2, float y2, float fm) { 
  float f = (y2 - y1) * (x2 - x1);
  float a = y1 - x1 * f;
  float x = (fm - a) / f;
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
      
        vec2 ul_p = vec2(0.0,1.0);
          //vec2 um_p = vec2(0.5,1.0);
          vec2 um_p = vec2(0.5, 1.0 + inb(fy, mm, fy+1, um, mm_f) - fy);
        vec2 ur_p = vec2(1.0,1.0);
      
          //vec2 ml_p = vec2(0.0, 0.5);
          vec2 ml_p = vec2(inb(fx, mm, fx-1, ml, mm_f) - fx, 0.5);
          //vec2 mr_p = vec2(1.0, 0.5);
          vec2 mr_p = vec2(1.0+inb(fx, mm, fx+1, mr, mm_f) -fx, 0.5);
 
        vec2 dl_p = vec2(0.0, 0.0);
          //vec2 dm_p = vec2(0.5, inb(fy, 0));
          vec2 dm_p = vec2(0.5, inb(fy, mm, fy-1, dm, mm_f) - fy);
        vec2 dr_p = vec2(1.0, 0.0);

      
      //Diagonal Left Down 
      if (ml_h && !mm_h && dl_h && dm_h || !ml_h && mm_h && !dl_h && !dm_h ) {
        line(ml_p, dm_p);
      } 
      //Diagonal Left Up
      if (ul_h && um_h && ml_h && !mm_h || !ul_h && !um_h && !ml_h && mm_h ) {
        line(ml_p, um_p);
      }
      //Diagonal Right Down
      if (!mm_h && mr_h && dm_h && dr_h || mm_h && !mr_h && !dm_h && !dr_h ) {
        line(dm_p, mr_p);
      }
      //Diagonal Right Up
      if (um_h && ur_h && !mm_h && mr_h || !um_h && !ur_h && mm_h && !mr_h ) {
        line(um_p, mr_p);
      }
      //Vertical Left Up
      if (ul_h && !um_h && ml_h && !mm_h || !ul_h && um_h && !ml_h && mm_h ) {
        line(ml_p, ul_p);
      }
      //Vertical Left Down
      if (ml_h && !mm_h && dl_h && !dm_h || !ml_h && mm_h && !dl_h && dm_h ) {
        line(dl_p, ml_p);
      }
      //Vertical Right Up
      if (um_h && !ur_h && mm_h && !mr_h || !um_h && ur_h && !mm_h && mr_h) {
        line(mr_p, ur_p); 
      }
      //Vertical Right down
      if (mm_h && !mr_h && dm_h && !dr_h ||  !mm_h && mr_h && !dm_h && dr_h) {
        line(dr_p, mr_p);
      }
      //Horizontal Down Left
      if (ml_h && mm_h && !dl_h && !dm_h || !ml_h && !mm_h && dl_h && dm_h) {
        line(dl_p, dm_p);
      }
      //Horizontal Down Right
      if (mm_h && mr_h && !dm_h && !dr_h || !mm_h && !mr_h && dm_h && dr_h)  {
        line(dm_p, dr_p);
      }
      //Horizontal Up Left  
      if (ul_h && um_h && !ml_h && !mm_h || !ul_h && !um_h && ml_h && mm_h)  {
        line(ul_p, um_p);
      }
      //Horizontal Up Right 
      if (um_h && ur_h && !mm_h && !mr_h || !um_h && !ur_h && mm_h && mr_h)  {
        line(um_p, ur_p);
      }
    }
  }
}
