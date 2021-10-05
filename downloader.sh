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
    git clone https://github.com/junkawahara/dd_package/raw/main/Makefile
    if [ $? -ne 0 ]; then exit; fi
fi

if [ -e main.cpp ]; then
    echo "main.cpp already exists."
else
    git clone https://github.com/junkawahara/dd_package/raw/main/main.cpp
    if [ $? -ne 0 ]; then exit; fi
fi
