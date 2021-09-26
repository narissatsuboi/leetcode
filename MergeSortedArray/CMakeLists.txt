cmake_minimum_required(VERSION 3.17)
project(MergeSortedArray)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++17 -W -Wall -pedantic")

add_executable(MergeSortedArray main.cpp)