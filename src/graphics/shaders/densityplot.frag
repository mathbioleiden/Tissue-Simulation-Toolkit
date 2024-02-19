#version 430 core
in vec4 gl_FragCoord;
out vec4 color;
layout (location = 2) uniform vec3 size;
layout (location = 6) uniform vec2 windowSize;
layout (location = 5) uniform samplerBuffer density;

in Data {
  vec4 col;
} cin;


void main(){
  vec2 pos = gl_FragCoord.xy / windowSize.xy * size.xy;
 
  float val = texelFetch(density, int(pos.x)*int(size.y)+int(pos.y)).r;  
  color = vec4(val, val, val, 1);
  color = cin.col;
  color.a = val/(val+1);
}
