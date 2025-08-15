cmake_minimum_required(VERSION 3.16)

project(tabby LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(CMAKE_CXX_COMPILER /usr/bin/g++)

set(PYBIND11_FINDPYTHON ON)
find_package(pybind11 CONFIG REQUIRED)
file(GLOB SOURCES "cpp/src/*.cpp")

pybind11_add_module(tabby ${SOURCES})

# pybind11_add_module(tabby main.cpp)
#install(TARGETS tabby DESTINATION .)

target_include_directories(tabby PRIVATE cpp/include)

add_executable(tabby_ex cpp/src/main.cpp)
