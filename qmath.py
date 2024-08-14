from __future__ import annotations
from math import sin, cos, atan2

class Cpx():
   real: float
   imag: float

   def __init__(self, a: float, b: float=0, **kwargs):
      assert isinstance(a, float|int)
      assert isinstance(b, float|int)
      if 'polar' in kwargs.keys() and kwargs['polar']:
         self.real = cos(b)*a
         self.imag = sin(b)*a
      else:
         self.real = a
         self.imag = b
    
   def __str__(self) -> str:
      return f"{self.real:.2f} + {self.imag:.2f}i"
   
   def __add__(self, val):
      z = val if isinstance(val, Cpx) else Cpx(val)
      return Cpx(self.real + z.real, self.imag + z.imag)

   def __sub__(self, val):
      z = val if isinstance(val, Cpx) else Cpx(val)
      return Cpx(self.real-z.real, self.imag-z.imag)

   def __mul__(self, val):
      z = val if isinstance(val, Cpx) else Cpx(val)
      a, b = self.real, self.imag
      c, d = z.real, z.imag
      return Cpx(a*c - b*d, a*d + b*c)

   def __div__(self, val):
      z = val if isinstance(val, Cpx) else Cpx(val)
      u, v = self, self.imag
      x, y = z.real, z.imag
      return Cpx( (u*x + v*y)/(z.mag()), (v*x-u*y)/(z.mag()) )
    
   def mag(self):
      return (self.real**2 + self.imag**2)**0.5
   
   def con(self):
      return Cpx(self.real, -self.imag)

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
         self.elements = list(map(lambda x: x if isinstance(x, Cpx) else Cpx(x), elements))
      
      self.cols = cols
      self.rows = rows
      
   def __getitem__(self, key):
      row, col = key
      return self.elements[self.cols*row+col]

   def __setitem__(self, key, val: Cpx):
      row, col = key
      self.elements[self.cols*row+col] = val if isinstance(val, Cpx) else Cpx(val)

   def __str__(self) -> str:
      s = '\n'.join(
         f'| {",  ".join(map(str, self.elements[i : i+self.cols]))} |'
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

   def __add__(self, m: Mtx):
      r, c = self.rows, self.cols
      assert r == m.rows and c == m.cols
      res = Mtx(r, c)
      for i in range(r):
         for j in range(c):
            res[i, j] = self[i, j] + m[i, j]
      return res

   def __sub__(self, m: Mtx):
      r, c = self.rows, self.cols
      assert r == m.rows and c == m.cols
      res = Mtx(r, c)
      for i in range(r):
         for j in range(c):
            res[i, j] = self[i, j] - m[i, j]
      return res

   def scal(self, n: Cpx):
      r, c = self.rows, self.cols
      m = Mtx(r, c)
      for i in range(r):
         for j in range(c):
            m[i, j] = self[i, j] * Cpx(n)
      return m

   def __mul__(self, m: Mtx):
      assert self.cols == m.rows
      res = Mtx(self.rows, m.cols)
      for i in range(res.rows):
         for j in range(res.cols):
            s = Cpx(0)
            for k in range(self.cols):
               s += self[i, k]*m[k, j]
            res[i, j] = s
      return res

   def ten(self, m: Mtx):
      r, c = self.rows*m.rows, self.cols*m.cols
      res = Mtx(r, c)
      for i in range(r):
         for j in range(c):
            res[i, j] = self[i//self.rows, j//self.cols] * m[i%m.rows, j%m.cols]
      return res
      
