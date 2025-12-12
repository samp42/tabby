#ifndef DATA_FRAME_H_
#define DATA_FRAME_H_

#include <vector>
#include "schema.h"
#include "series.h"

namespace tabby
{

    class DataFrame
    {
    public:
        DataFrame();
        ~DataFrame();

    private:
        Schema schema_;
        std::vector<Series> columns_;
    };

    std::unique_ptr<DataFrame> Concat(std::unique_ptr<DataFrame> d1, std::unique_ptr<DataFrame> d2);

} // namespace tabby

#endif // DATA_FRAME_H_
