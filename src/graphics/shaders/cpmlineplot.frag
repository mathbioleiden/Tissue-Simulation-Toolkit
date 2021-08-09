#version 430 core
in vec4 gl_FragCoord;
out vec4 color;
layout (location = 2) uniform vec3 size;
layout (location = 6) uniform vec2 windowSize;
layout (location = 9) uniform float l_width;

in Data {
  vec4 col;
} cin;

layout (std430, binding=7) buffer data{
  int intdata[];
};

void main(){
  vec2 pos = gl_FragCoord.xy / windowSize.xy * size.xy;
  int x = int(pos.x);
  int y = int(pos.y);

  int sx = int(size.x);
  int sy = int(size.y);
  
  int id = intdata[x*sy+y];
  int rid = id;
  int lid = id;
  int uid = id;
  int did = id;

  if (x != size.x ) rid = intdata[(x+1)*sy+y];
  if (x != 0 ) lid = intdata[(x-1)*sy+y];
  if (y != size.y ) uid = intdata[x*sy+(y+1)];
  if (y != 0 ) did = intdata[x*sy+(y-1)];

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

