#ifndef CHUNKED_ARRAY_H_
#define CHUNKED_ARRAY_H_

#include <memory>
#include <vector>
#include "array.h"
#include "types.h"

template <typename T>
class ChunkedArray
{
public:
    ChunkedArray(Types type, int chunkSize = 1024);
    ~ChunkedArray();

    void Append(const void *data, int size);
    void *Get(int index) const;
    int Length() const;

    Types GetType() const;

private:
    Types type_;
    int chunkSize_;
    std::vector<Array<T, chunkSize>> chunks_;
    int length_ = 0;

    void EnsureCapacity(int index);
};

#endif // CHUNKED_ARRAY_H_
