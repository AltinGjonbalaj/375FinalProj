all: inputgen

inputgen: input_generator.cpp
	g++ -g -Wall -Werror -o inputgen input_generator.cpp

.PHONY: clean all

clean:
	rm -rf inputgen
