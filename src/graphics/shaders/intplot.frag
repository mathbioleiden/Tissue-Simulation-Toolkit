#version 430 core
in vec4 gl_FragCoord;
out vec4 color;
layout (location = 2) uniform vec3 size;
layout (location = 6) uniform vec2 windowSize;
layout (location = 7) uniform isamplerBuffer intdata;

layout (std140, binding = 8) uniform colortable {
  vec4 coltable[300]; 
};


in Data {
  vec4 col;
} cin;


void main(){
  vec2 pos = gl_FragCoord.xy / windowSize.xy * size.xy;
  int id = texelFetch(intdata, int(pos.x)*int(size.y)+int(pos.y)).r;

  if (id > 0) {
    color = coltable[id];
  }
  if (id <= 0) {
    color = vec4(0,0,0,0);
  }
}
