class Vecteur2D :
    _count = 0
    def __init__(self, X = 1.5, Y = 2):
        self.__X = X
        self.__Y = Y
        self._count += 1

    # getter for X
    def GetX(self):
        return self.__X

    # getter for Y
    def GetY(self):
        return self.__Y
    
    # getter for _count
    def Getcount(self):
        return self._count

    # setter for X
    def SetX(self, X1):
        self.__X = X1

    # setter for Y
    def SetY(self, Y1):
        self.__Y = Y1

    # return string representation of vector
    def ToString(self):
        return "X = " + str(self.GetX()) + " Y = " + str(self.GetY())
    
    # check if two vectors are equal
    def Equals(self, vecteur1) :
        if vecteur1.GetX() == self.GetX() and vecteur1.GetY() == self.GetY() :
            return True
        else : 
            return False 
        
    # calculate the norm of the vector
    def Norme (self) :
        return (self.GetX()**2 + self.GetY()**2)**0.5

class Vecteur3D (Vecteur2D) :
    def __init__(self, X = 1.5, Y = 2, Z = 5) :
        super().__init__(X, Y)
        self.__Z = Z
        self._count += 1

    # getter for Z
    def GetZ(self):
        return self.__Z

    # setter for Z
    def SetZ(self, Z1):
        self.__Z = Z1

    # return string representation of vector
    def ToString(self):
        return "X = " + str(self.GetX()) + " Y = " + str(self.GetY()) + " Z = " + str(self.GetZ())

    # check if two vectors are equal
    def Equals(self, vecteur1) :
        if vecteur1.GetX() == self.GetX() and vecteur1.GetY() == self.GetY() and vecteur1.GetZ() == self.GetZ() :
            return True
        else : 
            return False 
        
    # calculate the norm of the vector
    def Norme (self) :
        return (self.GetX()**2 + self.GetY()**2 + self.GetZ()**2)**0.5