#ifndef ARRAY_H_
#define ARRAY_H_

#include <array>
#include <memory>
#include <stddef.h>

template <typename T, size_t Capacity>
using TabbyArray = std::unique_ptr<std::array<T, Capacity>>;

#endif // ARRAY_H_
