#ifndef SCHEMA_H_
#define SCHEMA_H_

#include <map>
#include <string>
#include "data_type.h"

namespace tabby
{
    using Schema = std::map<std::string, DataType>;
} // namespace tabby

#endif // SCHEMA_H_
