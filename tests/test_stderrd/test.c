#include <stdio.h>
int main(int argc,char * argv[])
{
    fprintf(stdout,BUILD_TARGET ":This is STDOUT test\n");
    fprintf(stderr,BUILD_TARGET ":This is STDERR test\n");
    return 0;
}
