#ifndef ARRAY_H_
#define ARRAY_H_

#include <memory>
#include "types.h"

template <typename T>
class Array
{
public:
    Array(int size);
    ~Array();

    T &operator[](int index);
    const T &operator[](int index) const;

    int Length() const;

private:
    std::unique_ptr<T[]> data_;
    int length_ = 0;
    int capacity_ = 0; // Default capacity
};

#endif // ARRAY_H_
