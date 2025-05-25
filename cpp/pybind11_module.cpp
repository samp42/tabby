#include <pybind11/pybind11.h>

namespace py = pybind11;

PYBIND11_MODULE(tabby, m)
{
    m.doc() = "pybind11 module for tabby";
}
