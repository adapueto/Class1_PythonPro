formula1_dict = {
            "LAPS": "Son las vueltas que haya dado los autos",
            "TYRES": "Tipo de ruedas que hay, por ejemplo: soft, hard, medium, wet, intermediate",
            "BOX": "Van al pit para cambiar las ruedas, hacer la sanción, o irse de la carrera por algun motivo",
            "FIA": "Federacion Internacional de automivilismo",
            "POLE POSICION": "Esta en el primer lugar",
            }

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in formula1_dict.keys():
    print(formula1_dict[word])
else:
    print("lo lamento se ve que no tenemos esa palabra")
