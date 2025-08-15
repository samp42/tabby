#include <pybind11/pybind11.h>

#include "csv.h"

namespace py = pybind11;

PYBIND11_MODULE(tabby, m)
{
    m.doc() = "pybind11 module for tabby";

    // m.def("read_csv", &tabby::ReadCSVRead, "A function that reads a CSV and returns a DataFrame", py::arg("path"));
}
