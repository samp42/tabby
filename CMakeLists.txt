cmake_minimum_required(VERSION 3.16)

project(tabby LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(PYBIND11_FINDPYTHON ON)
find_package(pybind11 CONFIG REQUIRED)

pybind11_add_module(tabby main.cpp)
#install(TARGETS tabby DESTINATION .)

#add_executable(tabby main.cpp)
