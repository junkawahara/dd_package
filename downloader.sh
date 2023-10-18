if ! type git > /dev/null 2>&1; then
    echo "Install git before running this script."
    exit
fi

if ! type make > /dev/null 2>&1; then
    echo "Install make before running this script."
    exit
fi

if [ x"$1" = 'x--update' ]; then


cd SAPPOROBDD
git pull
cd ../sbdd_helper
git pull
cd ../TdZdd
git pull
cd ..


else # not update

if [ -e SAPPOROBDD ]; then
    echo "SAPPOROBDD already exists."
else
    git clone https://github.com/Shin-ichi-Minato/SAPPOROBDD.git
    if [ $? -ne 0 ]; then exit; fi
fi

if [ -e TdZdd ]; then
    echo "TdZdd already exists."
else
    git clone https://github.com/kunisura/TdZdd.git
    if [ $? -ne 0 ]; then exit; fi
fi

if [ -e sbdd_helper ]; then
    echo "sbdd_helper already exists."
else
    git clone https://github.com/junkawahara/sbdd_helper.git
    if [ $? -ne 0 ]; then exit; fi
fi

# Fix SAPPOROBDD so that X11 does not get compiled.

if ! [ -e SAPPOROBDD/src/BDD+/Makefile.bak ]; then
    cp SAPPOROBDD/src/BDD+/Makefile SAPPOROBDD/src/BDD+/Makefile.bak
    sed -i -e 's#\$(DIR)/src/BDDXc/\*_32.o##' SAPPOROBDD/src/BDD+/Makefile
    sed -i -e 's#\$(DIR)/src/BDDXc/\*_64.o##' SAPPOROBDD/src/BDD+/Makefile
fi

if ! [ -e SAPPOROBDD/src/INSTALL.bak ]; then
    cp SAPPOROBDD/src/INSTALL SAPPOROBDD/src/INSTALL.bak
    sed -i -e "s#cd ../BDDXc##" SAPPOROBDD/src/INSTALL
fi

if ! [ -e SAPPOROBDD/src/BDDc/makefile.bak ]; then
    cp SAPPOROBDD/src/BDDc/makefile SAPPOROBDD/src/BDDc/makefile.bak
    sed -i -e 's#OPT   = -O3 -Wall -Wextra -Wshadow -I$(INCL)#OPT   = -O3 -Wall -Wextra -Wshadow -Wno-maybe-uninitialized -I$(INCL)#' SAPPOROBDD/src/BDDc/makefile
fi

#if [ -e SAPPOROBDD/lib/BDD64.a ]; then
#    echo "SAPPOROBDD build skipped because SAPPOROBDD/lib/BDD64.a exists"
#else
    cd SAPPOROBDD/src
    sh INSTALL
    cd ../../
#fi

if ! type curl > /dev/null 2>&1; then
    echo "Install curl for Makefile and main.cpp."
    exit
fi

if [ -e Makefile ]; then
    echo "Makefile already exists."
else
    curl -OL -Ss https://github.com/junkawahara/dd_package/raw/main/Makefile
    if [ $? -ne 0 ]; then exit; fi
fi

if [ -e main.cpp ]; then
    echo "main.cpp already exists."
else
    curl -OL -Ss https://github.com/junkawahara/dd_package/raw/main/main.cpp
    if [ $? -ne 0 ]; then exit; fi
fi


fi # update
