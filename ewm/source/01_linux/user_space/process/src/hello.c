#include <stdio.h>
#include <unistd.h>

int main()
{
    int idx = 0;

    while (1)
    {
        printf("Hello %d\n", idx++);
        sleep(1);
    }
    return 0;
}
