cmake_minimum_required(VERSION 3.17)
project(MaxConsectiveOnes)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -W -Wall -Werror -pedantic")

add_executable(MaxConsectiveOnes main.cpp)