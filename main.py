from qmath import *
def main():
   v0 = Mtx(1, 2**2)
   v0[0, 0] = 1

   H = Mtx(2, 2, [1, 1,
                  1, -1]).scal(1/(2**0.5))

   H2 = H.ten(H)

   CX = Mtx(4, 4)
   CX[0, 0] = 1
   CX[1, 1] = 1
   CX[2, 3] = 1
   CX[3, 2] = 1
    
   X = Mtx(2, 2, [0, 1,
                  1, 0])
   
   X2 = X.ten(X)


   I = Mtx(2, 2)
   I[0, 0] = 1
   I[1, 1] = 1


   v1 = v0 * H.ten(I) 
   v2 = v1 * CX

   print(v2)

    
main()
