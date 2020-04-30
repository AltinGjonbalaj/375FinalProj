all: inputgen sparseinputgen

inputgen: input_generator.cpp
	g++ -g -Wall -Werror -o inputgen input_generator.cpp

sparseinputgen: sparse_input_gen.cpp
	g++ -g -Wall -Werror -o sparseinputgen sparse_input_gen.cpp

.PHONY: clean all 

clean:
	rm -rf inputgen sparseinputgen *.o
