#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>
#include <string>

namespace py = pybind11;

// C++函数示例
int add(int a, int b) {
    return a + b;
}

double multiply(double a, double b) {
    return a * b;
}

std::vector<int> create_vector(int size) {
    std::vector<int> vec;
    for (int i = 0; i < size; ++i) {
        vec.push_back(i * i);
    }
    return vec;
}

class Calculator {
public:
    Calculator() : value(0) {}
    
    void add(int x) { value += x; }
    void subtract(int x) { value -= x; }
    int get_value() const { return value; }
    
private:
    int value;
};

// Python模块定义
PYBIND11_MODULE(cpp_math, m) {
    m.doc() = "C++数学库的Python绑定";
    
    // 绑定简单函数
    m.def("add", &add, "两个整数相加", py::arg("a"), py::arg("b"));
    m.def("multiply", &multiply, "两个浮点数相乘", py::arg("a"), py::arg("b"));
    m.def("create_vector", &create_vector, "创建平方数向量", py::arg("size"));
    
    // 绑定类
    py::class_<Calculator>(m, "Calculator")
        .def(py::init<>())
        .def("add", &Calculator::add)
        .def("subtract", &Calculator::subtract)
        .def("get_value", &Calculator::get_value)
        .def("__repr__", [](const Calculator &c) {
            return "Calculator(value=" + std::to_string(c.get_value()) + ")";
        });
} 