#version 430 core
layout (location = 1) in vec3 pos;
layout (location = 2) uniform vec3 size;
layout (location = 3) in vec4 col;

out Data {
 vec4 col;
} cout;

void main() {
  gl_Position = vec4((pos/size - 0.5) * 2, 1);
  cout.col = col;  
}
