#ifndef CHUNKED_ARRAY_H_
#define CHUNKED_ARRAY_H_

#include <memory>
#include <vector>
#include "array.h"

namespace tabby
{

    constexpr size_t CHUNK_SIZE = 256;

    typedef struct c
    {
        std::array<char, CHUNK_SIZE / 8> null_mask_;
        std::array<char, CHUNK_SIZE / 8> valid_mask_;
    } Chunk;

    template <typename T, size_t ChunkSize>
    class ChunkedArray
    {
    public:
        ChunkedArray() : length_(0) {};
        ~ChunkedArray();

        template <size_t n>
        void Append(const std::array<T, n> &data);
        void Append(ChunkedArray<T, ChunkSize> *other);
        size_t Length() const;
        size_t NumChunks() const;

    private:
        size_t length_ = 0;
        std::vector<TabbyArray<T, ChunkSize>> chunks_;
    };
} // namespace tabby

#endif // CHUNKED_ARRAY_H_
