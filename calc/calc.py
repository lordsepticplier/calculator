def plus (a , b ) :
  return a + b
  
def subtract (a , b ) :
  return a - b

def multiply (a , b ) :
  return a * b
  
def calculate ( method , a , b ) :
  
  methods = {
    'plus': plus ,
    'subtract': subtract,
    'multiply': multiply
  }
  return methods[method]( a , b )
