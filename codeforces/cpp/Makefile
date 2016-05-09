F = fbhrA.cpp
EXE = program
EXER = ./program

run: $(EXE)
	$(EXER)

program: $(F)
	g++ -Wall $? -o $@

clean:
	rm *.o $(EXE)