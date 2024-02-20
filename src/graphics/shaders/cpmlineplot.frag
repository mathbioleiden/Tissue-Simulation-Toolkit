#version 430 core
in vec4 gl_FragCoord;
out vec4 color;
layout (location = 2) uniform vec3 size;
layout (location = 6) uniform vec2 windowSize;
layout (location = 7) uniform isamplerBuffer intdata;
layout (location = 9) uniform float l_width;

in Data {
  vec4 col;
} cin;

void main(){
  vec2 pos = gl_FragCoord.xy / windowSize.xy * size.xy;
  int x = int(pos.x);
  int y = int(pos.y);

  int sx = int(size.x);
  int sy = int(size.y);
  
  int id = texelFetch(intdata, x*sy+y).r;
  int rid = id;
  int lid = id;
  int uid = id;
  int did = id;

  if (x != size.x ) rid = texelFetch(intdata, (x+1)*sy+y).r;
  if (x != 0 ) lid = texelFetch(intdata, (x-1)*sy+y).r;
  if (y != size.y ) uid = texelFetch(intdata, x*sy+(y+1)).r;
  if (y != 0 ) did = texelFetch(intdata, x*sy+(y-1)).r;

  float right = ceil(pos.x) - pos.x;
  float left  = pos.x - floor(pos.x);
  float up = ceil(pos.y) - pos.y;
  float down  = pos.y - floor(pos.y);
 
  color = cin.col; 
  if (right < l_width && rid != id || left < l_width && lid != id 
      || up < l_width && uid != id  || down < l_width && did != id) {
    color.a = 1;
  }
  else {
    color.a = 0;
  }
}

