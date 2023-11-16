#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv)
{
	char line[8192];
	unsigned long num;
	unsigned long day;
	unsigned long month;
	unsigned long year;
	FILE* file = fopen(argv[1], "r");
	unsigned long minYear = (unsigned long)atoi(argv[2]);

	// Read the first line with the field names, and output it
	fgets(line, 8192, file);
	printf("%s", line);

	while (fgets(line, 8192, file) != NULL) {
		sscanf(line, "%lu,%2lu/%2lu/%4lu,", &num, &day, &month, &year);
		if (year <= minYear) {
			printf("%s", line);
		}
	}

	fclose(file);
}
