#ifndef ARRAY_H_
#define ARRAY_H_

#include <array>

template <typename T, typename Capacity>
using Array = std::array<T, Capacity::value>;

#endif // ARRAY_H_
