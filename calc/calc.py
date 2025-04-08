def plus (a , b ) :
  return a + b
  
def subtract (a , b ) :
  return a - b
  
def calculate ( method , a , b ) :
  
  methods = {
    'add': add ,
    'subtract': subtract
  }
  if method not in methods :
    raise ValueError ( f " Unsupported method : { method } " )
  return methods [ method ]( a , b )
