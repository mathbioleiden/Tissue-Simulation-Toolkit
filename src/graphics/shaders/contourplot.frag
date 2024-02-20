#version 430 core

in vec4 gl_FragCoord;
out vec4 color;
layout (location = 2) uniform vec3 size;
layout (location = 6) uniform vec2 windowSize;
layout (location = 5) uniform samplerBuffer density;
layout (location = 9) uniform float l_width;


in Data {
  vec4 col;
} cin;


  vec2 point0;
  bool ul_h = false;
  bool ur_h = false;
  bool dl_h = false;
  bool dr_h = false;
  float ul = 0;
  float ur = 0;
  float dl = 0;
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


bool checkp(int a, int b, int c, int d){
  return ul_h == bool(a) && ur_h == bool(b) && dl_h == bool(c) && dr_h == bool(d) || ul_h == !bool(a) && ur_h == !bool(b) && dl_h == !bool(c) && dr_h == !bool(d); 
}


void make_profile(float mm_f) {
  ul_h = ul > mm_f;
  ur_h = ur > mm_f;
  dl_h = dl > mm_f;
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
  int x = int(round(fx));
  int y = int(round(fy));
  float o_ix = fx - float(x); 
  float o_iy = fy - float(y);
  int sx = int(size.x);
  int sy = int(size.y);
  
  float ix = o_ix;
  float iy = o_iy;

  if (o_ix < 0.5 && o_iy >= 0.5 ) {
    ix += 0.5;
    iy -= 0.5;
    x -= 1;
    y += 1;
  } else
  if (o_ix > 0.5 && o_iy >= 0.5 ) {
    ix -= 0.5;
    iy -= 0.5;
    y += 1;
  } else
  if (o_ix < 0.5 && o_iy < 0.5 ) {
    ix += 0.5;
    iy += 0.5;
    x -= 1;
  } else
  if (o_ix >= 0.5 && o_iy < 0.5 ) {
    ix -= 0.5;
    iy += 0.5;
  }

  point0 = vec2(ix, iy); 

  ul = texelFetch(density, (x)*sy+(y)).r;
  if (y != 0) dl = texelFetch(density, (x)*sy+(y-1)).r;
  if (x != sx - 1 && sy != 0) dr = texelFetch(density, (x+1)*sy+(y-1)).r;
  if (x != sx - 1) ur = texelFetch(density, (x+1)*sy+(y)).r;
  
  color = cin.col; 
  color.a = 0;
  int res = 0;
 
  int start = int(ul) - 1; 
   
  for (float mm_f = float(start); mm_f < start + 4;  mm_f++){
    if (!(mod(mm_f, 3) == 0 && int(mm_f) > 1)) continue;
    make_profile(mm_f);
 
    vec2 um = vec2(inb(0, ul, 1, ur, mm_f), 1.0);
    vec2 ml = vec2(0.0, inb(0, dl, 1, ul, mm_f));
    vec2 mr = vec2(1.0, inb(0, dr, 1, ur, mm_f) );
    vec2 dm = vec2(inb(0, dl, 1, dr, mm_f), 0.0);
   
    if (ul_h && ur_h && !dl_h && !dr_h || !ul_h && !ur_h && dl_h && dr_h  ) line(ml, mr);
    if (ul_h && !ur_h && dl_h && !dr_h || !ul_h && ur_h && !dl_h && dr_h  ) line(um, dm);

    if (ul_h && ur_h && !dl_h && dr_h || !ul_h && !ur_h && dl_h && !dr_h  ) line(ml, dm);
    if (ul_h && ur_h && dl_h && !dr_h || !ul_h && !ur_h && !dl_h && dr_h  ) line(dm, mr);
    if (ul_h && !ur_h && !dl_h && !dr_h || !ul_h && ur_h && dl_h && dr_h  ) line(ml, um);
    if (ul_h && !ur_h && dl_h && dr_h || !ul_h && ur_h && !dl_h && !dr_h  ) line(um, mr);
  }
}
