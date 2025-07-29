cmake_minimum_required(VERSION 3.10)

# 设置项目名称
project(HelloWorld)

# 设置C++标准为C++17
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 设置编译器为LLVM (通过Homebrew安装)
set(CMAKE_C_COMPILER /opt/homebrew/opt/llvm/bin/clang)
set(CMAKE_CXX_COMPILER /opt/homebrew/opt/llvm/bin/clang++)

# 设置LLVM的库和头文件路径
set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -L/opt/homebrew/opt/llvm/lib")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -I/opt/homebrew/opt/llvm/include")

# 添加include目录
include_directories(include)

# 添加可执行文件
add_executable(temp_convert src/temp_convert.cpp)
add_executable(odd_and_even src/odd_and_even.cpp)
add_executable(main src/main.cpp)
add_executable(break_time src/break_time.cpp)
add_executable(cube_number src/cube_number.cpp)
add_executable(simple_paint src/simple_paint.cpp)
add_executable(paint_brush src/paint_brush.cpp)
add_executable(buy_stationery src/buy_stationery.cpp)
add_executable(lucky_number src/lucky_number.cpp)
