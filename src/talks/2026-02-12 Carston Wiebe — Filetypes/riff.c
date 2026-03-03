#include <stdio.h>
#include <stdlib.h>
#include <sysexits.h>
#include <stdbool.h>

unsigned int readRiff(FILE* file)
{
    static unsigned int level = 0;

    unsigned char id[5] = {0};

    if (!fread(id, 4, 1, file)) {
        printf("invalid data\n");
        exit(EX_DATAERR);
    }

    unsigned char buf[4] = {0};
    fread(buf, 4, 1, file);
    unsigned int size = buf[0] | (buf[1] << 8) | (buf[2] << 16) | (buf[3] << 24);

    bool isList =
        id[0] == 'R' && id[1] == 'I' && id[2] == 'F' && id[3] == 'F'
     || id[0] == 'L' && id[1] == 'I' && id[2] == 'S' && id[3] == 'T'
     || id[0] == 'C' && id[1] == 'A' && id[2] == 'T' && id[3] == ' ';

#define PRINT_INDENTED(...) \
    for (int i = 0; i < level; i++) printf("|___ "); \
    printf(__VA_ARGS__);

    PRINT_INDENTED("id   %s\n", id);
    PRINT_INDENTED("size %u\n", size);

    if (isList) {
        unsigned char name[5] = {0};
        fread(name, 4, 1, file);

        PRINT_INDENTED("name %s\n", name);

        unsigned int remaining = size - 4;

        level++;
        while (remaining > 0) {
            unsigned int childSize = readRiff(file);
            remaining -= childSize + 8;
        }
        level--;
    } else {
        unsigned char* data = calloc(size, 1);
        fread(data, size, 1, file);
        // do stuff...
        free(data);
    }

    if (size % 2) {
        fgetc(file);
    }

    PRINT_INDENTED("end  %s\n", id);

    return size;
}

int main(int argc, char** argv)
{
    if (argc != 2) {
        printf("no input file\n");
        return EX_USAGE;
    }

    FILE* file = fopen(argv[1], "r");

    if (!file) {
        printf("bad input file\n");
        return EX_NOINPUT;
    }

    readRiff(file);

    fclose(file);
    return 0;
}
