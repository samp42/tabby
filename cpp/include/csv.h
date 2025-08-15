#ifndef TABBY_H_
#define TABBY_H_

#include <iostream>
#include <fstream>
#include <string>
#include "data_frame.h"
#include "schema.h"

namespace tabby
{

    enum ReadAlgorithm
    {
        READ,
        MMAP_SINGLE_THREADED,
        MMAP_MULTI_THREADED
    };

    // DataFrame *ReadCSV(std::string path, Schema schema, ReadAlgorithm readAlgorithm);

    std::unique_ptr<DataFrame> ReadCSVRead(std::string path, Schema schema);

    // 1. Get File descriptor

    // 2. mmap file

    // 3. Read bytes

    // 4. Parse

    // 5. Collect to DataFrame
    // DataFrame *ReadCSV_MMAP_SINGLE_THREADED(std::string path, Schema schema);

    // DataFrame *ReadCSV_MMAP_MULTI_THREADED(std::string path, Schema schema);

    // DataFrame *ParseLine(std::string line, Schema schema);

} // tabby

#endif // TABBY_H_
