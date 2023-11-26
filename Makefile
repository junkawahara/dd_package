OPT = -O3 -DB_64 -I. -ISAPPOROBDD/include -ITdZdd/include

main: main.cpp SAPPOROBDD/lib/BDD64.a
	g++ $(OPT) main.cpp SAPPOROBDD/lib/BDD64.a -o main

# If you want to use GMP, use this.
main-gmp: main.cpp SAPPOROBDD/lib/BDD64.a
	g++ $(OPT) -DSBDDH_GMP main.cpp SAPPOROBDD/lib/BDD64.a -lgmp -lgmpxx -o main-gmp

clean:
	rm -rf *.o
