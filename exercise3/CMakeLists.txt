cmake_minimum_required(VERSION 3.14)
project(exercise3 C)

set(CMAKE_C_STANDARD 11)

target_link_libraries(exercise3 math)
add_executable(exercise3 main.c)
