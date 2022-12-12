import random

if True:
    print("la condition est vraie")
    print("Ce code est exécuté")

    if False:
        print("la condition est fausse")
        print ("Ce code n'est pas epythxécuté")

        condition_vente = True

        if conditions_vente:
            print("L'utilisateur accepté les conditions de vente")
        else:
          print("L'utilisateur n'a pas accepté les conditions de vente")

        if not condition_vente:
                print ("L'utilisateur n'a pas accepté les conditions de vente")
        else:
               print ("L'utilisateur a accepté les conditions de vente")
                    
            

        if  emails ==1:
            print("Vous avez un nouveau mail")
        elif emails> 1:
             print(f"Vous avez{emails}nouveaux emails")
        else: print("Vous n'avez pas de nouveaux mail")

        emails = 0
        print(0)

        #elif c'est la meme chose else if
        if emails == 1:
            print("vous avez un nouveaux mails")
        elif emails > 1:
         print(f"vous avez {emails}nouveau mails")
         if emails == 0:
            print("vous n'avez pas de nouveaux mails")

windows_closed = bool(random.randint(0,1))
electricity_off = bool (random.randint (0,1))


     print(f'{widows_closed =}')
     print(f'{electricity_off = }')
     

if windows_closed and electricity_off:
    print("Les fenêtres sont fermées")
    print("L'électricité est coupée")
elif not windows_closed an electricity_off:
    print("Les fenêtre ne sont pas fermées") 
    print("l'électricité est coupée")

elif windows_closed and not electricity_off:
    print("Les fenêtres sont fermées")
    print("L'électricité n'est pas coupée")   




else: 
    print("Les fenêtre ne sont pas fermées")
    print("L'électricité n'est pas coupée")
