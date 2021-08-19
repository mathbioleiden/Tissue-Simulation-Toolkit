#version 430 core
in vec4 gl_FragCoord;
out vec4 color;
layout (location = 2) uniform vec3 size;
layout (location = 6) uniform vec2 windowSize;

in Data {
  vec4 col;
} cin;

layout (std430, binding=5) buffer density{
  float dense[];
};

void main(){
  vec2 pos = gl_FragCoord.xy / windowSize.xy * size.xy;
 
  float val = dense[int(pos.x)*int(size.y)+int(pos.y)];
  
  color = cin.col;
  color.a = val/(val+1);
}
