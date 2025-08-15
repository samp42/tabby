#ifndef SERIES_H_
#define SERIES_H_

#include <string>
#include "chunked_array.h"
#include "data_type.h"

namespace tabby
{

    class Series
    {
    public:
        Series(std::string name);
        ~Series();

    private:
        std::string name_;
        DataType type_;
        ChunkedArray<T, CHUNK_SIZE> data_;
    };

} // namespace tabby

#endif // SERIES_H_
