def plus (a , b ) :
  return a + b
  
def subtract (a , b ) :
  return a - b
  
def calculate ( method , a , b ) :
  
  method = {
    ’ add ’: add ,
    ’ subtract ’: subtract
  }

  if method not in method :
    raise ValueError ( f " Unsupported method : { method } " )
  return method [ method ]( a , b )
