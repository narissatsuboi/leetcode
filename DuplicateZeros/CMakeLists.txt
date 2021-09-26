cmake_minimum_required(VERSION 3.17)
project(DuplicateZeros)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++17 -W -Wall -Werror -pedantic")

add_executable(DuplicateZeros main.cpp)