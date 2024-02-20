#version 430 core
in vec4 gl_FragCoord;
out vec4 color;
layout (location = 2) uniform vec3 size;
layout (location = 6) uniform vec2 windowSize;
//layout (location = 8) uniform vec4 coltable[300];

layout (std140, binding = 8) uniform colortable {
  vec4 coltable[300]; 
};


in Data {
  vec4 col;
} cin;

layout (std430, binding=7) buffer data{
  int intdata[];
};

void main(){
  vec2 pos = gl_FragCoord.xy / windowSize.xy * size.xy;
 
  int id = intdata[int(pos.x)*int(size.y)+int(pos.y)];

  if (id > 0) {
    color = coltable[id]; 
  }
  if (id <= 0) {
    color = vec4(0,0,0,0);
  }
}
