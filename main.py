from __future__ import annotations
from math import sin, cos, atan2

class Cpx():
   real: float
   imag: float

   def __init__(self, a: float, b: float=0, **kwargs):
      assert isinstance(a, float|int)
      assert isinstance(a, float|int)
      if 'polar' in kwargs.keys() and kwargs['polar']:
         self.real = cos(b)*a
         self.imag = sin(b)*a
      else:
         self.real = a
         self.imag = b
    
   def __str__(self) -> str:
      return f"{self.real:.2f} + {self.imag:.2f}i"
    
   @staticmethod
   def add(z1: Cpx, z2: Cpx):
      return Cpx(z1.real+z2.real, z1.imag+z2.imag)

   @staticmethod
   def sub(z1: Cpx, z2: Cpx):
      return Cpx(z1.real-z2.real, z1.imag-z2.imag)

   @staticmethod
   def mul(z1: Cpx, z2: Cpx):
      a, b = z1.real, z1.imag
      c, d = z2.real, z2.imag
      return Cpx(a*c - b*d, a*d + b*c)

   @staticmethod
   def div(z1: Cpx, z2: Cpx):
      u, v = z1, z1.imag
      x, y = z2.real, z2.imag
      return Cpx( (u*x + v*y)/(z2.mag()), (v*x-u*y)/(z2.mag()) )
    
   def mag(self):
      return (self.real**2 + self.imag**2)**0.5
   
   @staticmethod
   def con(z: Cpx):
      return Cpx(z.real, -z.imag)
   
   @staticmethod
   def scal(z: Cpx, n: float):
      return Cpx(z.real*n, z.imag*n)

   def angl(self):
      return atan2(self.imag, self.real)
    
   def copy(self):
      return Cpx(self.real, self.imag)

class Mtx():

   rows: int
   cols: int
   elements: list[Cpx]

   def __init__(self, rows: int, cols: int, elements: list = None):

      if elements == None:
         self.elements = [Cpx(0) for i in range(rows*cols)]
      else:
         assert len(elements) == rows * cols
         self.elements = elements
      
      self.cols = cols
      self.rows = rows
      
   def __getitem__(self, key):
      row, col = key
      return self.elements[self.rows*row+col]

   def __setitem__(self, key, val: Cpx):
      row, col = key
      self.elements[self.rows*row+col] = val

   def __str__(self) -> str:
      s = '\n'.join(
         f'| {',  '.join(map(str, self.elements[i : i+self.cols]))} |'
           for i in range(0, self.rows*self.cols, self.cols)
         )
      return s
   
   def copy(self):
      m = Mtx(self.rows, self.cols, [i.copy() for i in self.elements])
      return m
   
   def row(self, n: int):
      '''Counting starts with zero btw'''
      return [z.copy() for z in self.elements[n*self.cols:(n+1)*self.cols]]

   def col(self, n: int):
      '''Counting starts with zero btw'''
      return [z.copy() for z in self.elements[n:self.rows*self.cols:self.cols]]

   @staticmethod
   def add(m1: Mtx, m2: Mtx):
      r, c = m1.rows, m1.cols
      assert r == m2.rows and c == m2.cols
      res = Mtx(r, c)
      for i in range(r):
         for j in range(c):
            res[i, j] = Cpx.add(m1[i, j], m2[i, j])
      return res
   
   @staticmethod
   def sub(m1: Mtx, m2: Mtx):
      r, c = m1.rows, m1.cols
      assert r == m2.rows and c == m2.cols
      res = Mtx(r, c)
      for i in range(r):
         for j in range(c):
            res[i, j] = Cpx.sub(m1[i, j], m2[i, j])
      return res

   @staticmethod
   def scal(m1: Mtx, n: Cpx):
      r, c = m1.rows, m1.cols
      m = Mtx(r, c)
      for i in range(r):
         for j in range(c):
            m[i, j] = Cpx.scal(m1[i, j], n)
      return m

   @staticmethod
   def mul(m1: Mtx, m2: Mtx):
      assert m1.cols == m2.rows
      m = Mtx(m1.rows, m2.cols)
      for i in range(m.rows):
         for j in range(m.cols):
            row = m1.row(i)
            col = m2.col(j)
            c = Cpx(0)

            for k in range(len(row)):
               c = Cpx.add(c, Cpx.mul(row[k], col[k]))

            m[i, j] = c
      return m

   @staticmethod
   def ten(m1: Mtx, m2: Mtx):
      r, c = m1.rows*m2.rows, m1.cols*m2.cols
      m = Mtx(r, c)
      for i in range(r):
         for j in range(c):
            m[i, j] = Cpx.mul(m1[i//m1.rows, j//m1.cols], m2[i%m2.rows, j%m2.cols])
      return m
      
def main():
   m1 = Mtx(2, 2, [Cpx(1), Cpx(2), 
                   Cpx(3), Cpx(4)])
   
   m2 = Mtx(2, 2, [Cpx(5), Cpx(6), 
                   Cpx(7), Cpx(8)])
   
   m3 = Mtx(2, 3, [Cpx(1), Cpx(2), 
                   Cpx(3), Cpx(4),
                   Cpx(5), Cpx(6)])
   
   print(Mtx.mul(m1, m2))
   print(m1.mul(m2))
   

main()
