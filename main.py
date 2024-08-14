from qmath import *
def main():
    m1 = Mtx(2, 2, [Cpx(1), Cpx(2), 
                    Cpx(3), Cpx(4)])
   
    m2 = Mtx(2, 2, [Cpx(5), Cpx(6), 
                    Cpx(7), Cpx(8)])
   
    m3 = Mtx(2, 3, [Cpx(1), Cpx(2), 
                    Cpx(3), Cpx(4),
                    Cpx(5), Cpx(6)])

    v0 = Mtx(1, 4)
    v0[0, 0] = Cpx(1)

    H = Mtx(2, 2, [Cpx(1), Cpx(1),
                   Cpx(1), Cpx(-1)]).scal(2**0.5)

    CX = Mtx(4, 4)
    CX[0, 0] = Cpx(1)
    CX[1, 1] = Cpx(1)
    CX[2, 3] = Cpx(1)
    CX[3, 2] = Cpx(1)
    
    I = Mtx(2, 2)
    I[0, 0] = Cpx(1)
    I[1, 1] = Cpx(1)


    v1 = v0 * H.ten(I) 
    v2 = v1 * CX

    print(v2)

    
main()
