palabras_M = {"XD":"es una forma de expresar risa",
            "Spam":"es enviar muchas veces un objeto en concreto",
            "Meme":"es un chiste",
            "Cringe":"algo extraño"
            }
            
pregunta = input("¿Que palabra te gustaria conocer?")
if pregunta in palabras_M.keys():
    print(palabras_M[pregunta])
else:
    print("no tenemos esa palabra")
