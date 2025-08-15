#include <cmath>

#include "chunked_array.h"

namespace tabby
{

    template <typename T, size_t ChunkSize>
    template <size_t n>
    void ChunkedArray<T, ChunkSize>::Append(const std::array<T, n> &data)
    {

        // 1. Check that current chunks can accept more data and add to last chunk
        size_t availableLastChunk = this->chunks_.size() * ChunkSize - this->length_;
        if (availableLastChunk > 0)
        {
            // Add to last chunk
            if (n <= availableLastChunk)
            {
                std::copy(data.begin(), data.end(), this->chunks_.back()->begin());
            }
            else
            {
                std::copy(data.begin(), data.begin() + availableLastChunk, this->chunks_.back()->begin());
            }
        }

        // 2. Once last chunk is full, iteratively add chunks
        size_t additionalChunks = (size_t)std::ceil((n - availableLastChunk) / ChunkSize);

        for (size_t i = 0; i < additionalChunks; i++)
        {
            // if last chunk, check bound since chunk could be smaller
            // if (i == additionalChunks - 1)
            // {
            //     auto end = ;
            // }
            this->chunks_.emplace_back(std::make_unique<std::array<T, ChunkSize>>());
            // std::copy(data.begin() + availableLastChunk + i * this->chunkSize_, data.);
        }

        this->length_ += n;
    }

    template <typename T, size_t ChunkSize>
    void ChunkedArray<T, ChunkSize>::Append(ChunkedArray<T, ChunkSize> *other)
    {
        // 1. Align other's chunks

        // 2. Add other's chunks to this->chunks
    }

    template <typename T, size_t ChunkSize>
    size_t ChunkedArray<T, ChunkSize>::Length() const
    {
        return this->length_;
    }

    template <typename T, size_t ChunkSize>
    size_t ChunkedArray<T, ChunkSize>::NumChunks() const
    {
        return this->chunks_.size();
    }
}
