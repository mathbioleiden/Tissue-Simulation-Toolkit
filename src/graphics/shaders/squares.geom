#version 430 core
layout (points) in;
layout (triangle_strip, max_vertices = 6) out;
layout (location = 2) uniform vec3 size;

in Data {
  in vec4 col;
} cin[];

out Data {
  out vec4 col; 
} cout;

void main() {
    float ox = 1 / size.x * 2;  
    float oy = 1 / size.y * 2;

    gl_Position = gl_in[0].gl_Position;
    cout.col = cin[0].col;
    EmitVertex();

    gl_Position = gl_in[0].gl_Position + vec4(ox, 0, 0, 0);
    cout.col = cin[0].col;
    EmitVertex();

    gl_Position = gl_in[0].gl_Position + vec4(0, oy, 0, 0); 
    cout.col = cin[0].col;
    EmitVertex();
    EndPrimitive(); 
    
    gl_Position = gl_in[0].gl_Position + vec4(0, oy, 0, 0); 
    cout.col = cin[0].col;
    EmitVertex();

    gl_Position = gl_in[0].gl_Position + vec4(ox, 0, 0, 0); 
    cout.col = cin[0].col;
    EmitVertex();

    gl_Position = gl_in[0].gl_Position + vec4(ox, oy, 0, 0); 
    cout.col = cin[0].col;
    EmitVertex();
    EndPrimitive();
}  
