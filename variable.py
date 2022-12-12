   # l'operationd'affection =permet d'injecter une valeur dans une varéable

my_text1 = "ceci est une chaine de caractères"
my_text2 ='ceci est aussi une chaine de caractères'

print(my_text1)
print(my_text2)


my_number1 =142
my_number2 =65

print(my_number1 -my_number2)

# float, nombre a  virgule flottante
my_number3 = 3.14
my_number4 =-2.71
my_number5 = 0.0

print(my_number3)
print(my_number4)
print(my_number5)
print(type(my_number5))

 # bool, booléen

my_boolean1 = True 
my_boolean2 = False
print(my_boolean1)
print(my_boolean2)
print(type(my_boolean1))

# None , valeur nulle
# nul , nil

my_none = None
print(my_none)
print(type(my_none))

 #string, chaine de caractères
 #double quote ou simple quote , c'est pareil
my_text1 = "Ceci est une chaine de caractères"
my_text2 = 'Ceci est aussi une chaine de caractères'
      

print(my_text1)
print(my_text2)

 #  \ caractère d'échappement 
 #  \n saut de ligne

my_text3 = "abc\ndef\nghi"
my_text4 = "\\"
my_text5 = "John \"Foo\"Doe"

print(my_text3) 
print(my_text4)
print(my_text5)



a= 123
b= 42
# permutation de la valeur des variables 
a, b = b, a
print(a, b)

a= 123
b= 42

c=a 
a=b
b=

# transtypage
foo = "123"
#str vers int
foo = int(foo)
print(type(foo))

foo = 3.14
# flota vers int, permet de supprimer tout ce qui se trouve derrière la virgule
foo = int (foo)
print(foo)

foo = 3.14
foo = str (foo)
print(type(foo))


#
foo = 2.71
# récupérer la partie entière (c-a-d 2)
a =
# récupérer la partie aprés les virgules (c-a-d 0.71)
b =
print (a)
print (b)