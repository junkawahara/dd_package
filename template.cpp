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

    BDD_Init(1024, 1024 * 1024 * 1024);
    BDD_NewVar();

    DdStructure<2> dd;

    return 0;
}
