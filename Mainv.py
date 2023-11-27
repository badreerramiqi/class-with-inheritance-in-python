from class4 import Vecteur2D, Vecteur3D 
# import the Vecteur2D and Vecteur3D classes from the class4 module

vecteur0 = Vecteur2D() 
# create a new instance of the Vecteur2D class
vecteur1 = Vecteur2D(1.5, 3)
# create a new instance of the Vecteur2D class with the specified coordinates

print(vecteur0.ToString()) 
# print a string representation of the vector0
print(vecteur1.ToString()) 
# print a string representation of the vector1

print("l'abscisse et l'ordonne des deux vecteurs sont egaux :", vecteur0.Equals(vecteur1)) 
# compare the two vectors to see if they are equal

print("Norme de vecteur0 est :", vecteur0.Norme()) 
# calculate the norm (length) of the vector0
print("Norme de vecteur1 est :", vecteur1.Norme()) 
# calculate the norm (length) of the vector1

vecteur2 = Vecteur3D() 
# create a new instance of the Vecteur3D class
vecteur3 = Vecteur3D(1.5, 3, 5) 
# create a new instance of the Vecteur3D class with the specified coordinates

print(vecteur2.ToString()) 
# print a string representation of the vector2
print(vecteur3.ToString()) 
# print a string representation of the vector3

print("l'abscisse et l'ordonne des deux vecteurs sont egaux :", vecteur2.Equals(vecteur3)) 
# compare the two vectors to see if they are equal

print("Norme de vecteur2 est :", vecteur2.Norme()) 
# calculate the norm (length) of the vector2
print("Norme de vecteur3 est :", vecteur3.Norme()) 
# calculate the norm (length) of the vector3