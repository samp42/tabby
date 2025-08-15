// #include <memory>
// #include "csv.h"

// namespace tabby
// {

//     /*
//     DataFrame *ReadCSV(std::string path, Schema schema, ReadOption readOption)
//     {
//         switch (readOption)
//         {
//         case READ:
//             return ReadCSVRead(path);
//         default:
//             return nullptr;
//         }
//     }
//     */

//     std::unique_ptr<DataFrame> ReadCSVRead(std::string path, Schema schema)
//     {
//         std::unique_ptr<DataFrame> df = std::make_unique<DataFrame>();
//         std::ifstream csv(path);

//         std::string line;

//         while (getline(csv, line, '\n'))
//         {
//             auto lineDf = ParseLine(path, schema);
//             df = Concat(df, lineDf);
//         }

//         return df;
//     }

//     std::unique_ptr<DataFrame> ParseLine(std::string line, Schema schema)
//     {
//         std::unique_ptr<DataFrame> lineDf = std::make_unique<DataFrame>();

//         for (auto key : schema)
//         {
//         }

//         return lineDf;
//     }

// } // tabby
