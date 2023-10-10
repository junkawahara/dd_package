if ! type git > /dev/null 2>&1; then
    echo "Install git before running this script."
    exit
fi

if ! type make > /dev/null 2>&1; then
    echo "Install make before running this script."
    exit
fi

if ! type curl > /dev/null 2>&1; then
    echo "Install curl before running this script."
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

# Fix SAPPOROBDD so that X11 does not get compiled.

cp SAPPOROBDD/src/BDD+/Makefile SAPPOROBDD/src/BDD+/Makefile.bak
sed -i -e 's#\$(DIR)/src/BDDXc/\*_32.o##' SAPPOROBDD/src/BDD+/Makefile
sed -i -e 's#\$(DIR)/src/BDDXc/\*_64.o##' SAPPOROBDD/src/BDD+/Makefile

cp SAPPOROBDD/src/INSTALL SAPPOROBDD/src/INSTALL.bak
sed -i -e "s#cd ../BDDXc##" SAPPOROBDD/src/INSTALL

cd SAPPOROBDD/src
sh INSTALL
cd ../../

fi # update
