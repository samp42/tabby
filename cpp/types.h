#ifndef TYPES_H_
#define TYPES_H_

typedef enum
{
    Int32,
    Int64,
    Float32,
    Float64,
    String,
    Binary
} Types;

class Schema
{
public:
    Schema();

private:
};

template <typename T>
class Chunk
{
public:
    Chunk(T...);

private:
};

#endif // TYPES_H_
