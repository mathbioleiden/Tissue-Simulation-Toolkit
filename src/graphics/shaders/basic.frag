#version 430 core
out vec4 color;

in Data {
  vec4 col;
} cin;

void main(){
  color = cin.col;
}

