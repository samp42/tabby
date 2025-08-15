#include <iostream>
#include <array>

int main()
{
    std::array<int, 10> a = {1, 2, 3};

    std::cout << a.size() << std::endl;
    std::cout << a.max_size() << std::endl;

    for (const auto x : a)
    {
        std::cout << x << " ";
    }
    return 0;
}
