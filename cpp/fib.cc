#include <iostream>

struct fib;
struct fib1;
struct fib2;

struct fib
{
    int n;
    fib1 *f1;
    fib();
    int next();

    ~fib();
};

struct fib1
{
    int n;
    fib2 *f2;
    fib1();
    int next();

    ~fib1();
};

struct fib2
{
    fib *f;
    fib1 *f1;
    fib2();
    int next();

    ~fib2();
};

fib::fib(): n(0), f1(NULL) {}
int fib::next() {
    if (n == 0) {n = 1; return 1;}
    if (f1 == NULL) {f1 = new fib1();}
    return f1->next();
}

fib1::fib1(): n(0), f2(NULL) {}
int fib1::next() {
    if (n == 0) {n = 1; return 1;}
    if (f2 == NULL) {f2 = new fib2();}
    return f2->next();
}

fib2::fib2(): f(NULL), f1(NULL) {}
int fib2::next() {
    if (f == NULL) {f = new fib();}
    if (f1 == NULL) {f1 = new fib1();}
    return f->next() + f1->next();
}

fib::~fib() { if (f1) delete f1; }
fib1::~fib1() { if (f2) delete f2; }
fib2::~fib2() { if (f) delete f; if (f1) delete f1; }

int main() {
    fib f;
    for (int i = 0; i < 10; ++i)
    {
        std::cout << f.next() << std::endl;
    }
}
