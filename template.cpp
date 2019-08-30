#include "SAPPOROBDD/ZBDD.h"
#include "helper/SBDD_helper.h"

// delete commentout if necessary
//#include "tdzdd/DdEval.hpp"
#include "tdzdd/DdSpec.hpp"
//#include "tdzdd/DdSpecOp.hpp"
#include "tdzdd/DdStructure.hpp"

using namespace tdzdd;
using namespace sbddh;

int main() {

    // SAPPOROBDD functions

    BDD_Init(1024, 1024 * 1024 * 1024);
    BDD_NewVar();
    BDD_NewVar();

    ZBDD z1 = ZBDD(1);
    z1 = z1.Change(1);

    // SAPPOROBDD helper functions
    ZBDD z2 = getSingleton(1);

    //std::cout << (z1 == z3 ? "z1 == z3" : "z1 != z3") << std::endl;

    ZBDD z3 = getChild1(z2);

    //std::cout << "z3 is" << (isConstant(z3) ? " " : " not ") <<
    //    "constant" << std::endl;

    // tdzdd functions

    DdStructure<2> dd;
    NodeId node = dd.root();

    bool b = (z1 == z2 && isConstant(z3) && node.row() == 0 && node.col() == 0);
    std::cout << "program " << (b ? "works" : "does not work")
              << " correctly" << std::endl;

    return 0;
}
