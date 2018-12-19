import math

class Vector( object ):
    
    def __init__( self, x=0, y=0 ):
        
        self.__x = x
        self.__y   = y
        #self.__vector = 0

    def __str__( self ):
        
        out_str = "{:02d}{:02d}".format( self.__x, self.__y)
        return out_str

    def __repr__( self ):

        out_str = "{}{}".format( self.__x, self.__y)
        return out_str
    
    def __add__( self, vector ):

        vector=self.__x+self.__y
        return vector
    
    def __sub__( self, vector ):

        vector=self.__x-self.__y
        return vector
    
    def __mul__( self, vector ):

        vector=self.__x*self.__y
        return vector
    
    def __rmul__( self, vector ):

        vector=self.__x*self.__y
        return vector
    
    def __eq__( self, vector):
        
        vector=self.__x==self.__y#1 or 2
        return vector
    
    def magnitude( self ):
        
        return( float(math.sqrt(self.__x**2 + self.__y**2)))
        
    def unit( self ):
        
        
        if Vector.magnitude(self)==0:
            raise ValueError("Cannot convert zero vector to a unit vector")
            
        1/Vector.magnitude(self)