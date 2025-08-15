#include "data_frame.h"

namespace tabby
{

    std::unique_ptr<DataFrame> Concat(std::unique_ptr<DataFrame> d1, std::unique_ptr<DataFrame> d2)
    {
        if (d1 == nullptr && d2 == nullptr)
            return nullptr;

        if (d1 == nullptr)
            return d2;

        if (d2 == nullptr)
            return d1;

        // return d1->
        return nullptr;
    }

} // namespace tabby
