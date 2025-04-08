def plus (a , b ) :
  return a + b
  
def subtract (a , b ) :
  return a - b
  
def calculate ( method , a , b ) :
  
  methods = {
    'plus': plus ,
    'subtract': subtract
  }
  return methods[method]( a , b )
