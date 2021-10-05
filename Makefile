OPT = -O3 -DB_64 -I. -ISAPPOROBDD/include -ITdZdd/include

main: main.cpp SAPPOROBDD/lib/BDD64.a
	g++ $(OPT) main.cpp SAPPOROBDD/lib/BDD64.a -o main

clean:
	rm -rf *.o
