#Coleccion de paises:
paises = [
    {  
       "nombre": "Colombia",
       "capital": "Bogota",
       "moneda": "Peso Colombiano",
       "ciudades":
        [
          {
              "nombre": "Bogota",
              "poblacion": 8.2,
              "fundacion": 1538,
          },
          {
              "nombre": "Medellin",
              "poblacion": 8.2,
              "fundacion": 1675,
          },
          {
              "nombre": "Cali",
              "poblacion": 8.2,
              "fundacion": 1536,
          },
        
        ]
    },
    {
       "nombre": "Peru",
       "capital": "Lima",
       "moneda": "Sol",
       "ciudades":
        [
          {
               "nombre": "Lima",
               "poblacion": 10,
               "fundacion": 1535,
          },
          {
               
               "nombre": "Cuzco",
               "poblacion": 7.8,
               "fundacion": 1635,
          },

        ]
    },
    {
       "nombre": "Venezuela",
       "capital": "Caracas",
       "moneda": "Bolivar",
       "ciudades":
        [
          {
              
               "nombre": "Caracas",
               "poblacion": 9.8,
               "fundacion": 1463,
          },
          {
               
               "nombre": "Maracaibo",
               "poblacion": 8.3,
               "fundacion": 1515,
          },
        
        ]
    },
    {  
       "nombre": "Bolivia",
       "capital": "Sucre",
       "moneda": "Boliviano",
       "ciudades":
        [
          {
              
               "nombre": "Sucre",
               "poblacion": 8.5,
               "fundacion": 1325,
          },
          {
               
               "nombre": "La Paz",
               "poblacion": 4.6,
               "fundacion": 1368,
          },
        
        ]
    },
]

#Iterar cada pais
print("-------------------")
print("Recorrido de Paises")
print("-------------------")
for pais in paises:
    print("Nombre:" ,pais["nombre"])
    print("Capital:" ,pais["capital"])
    print("-------------------")
    print("Ciudades principales de:" ,pais["nombre"]) 
    for ciudad in pais["ciudades"]:
        print("--Ciudad",ciudad["nombre"])
        print("  Poblacion",ciudad["poblacion"])
        print("  Fundacion",ciudad["fundacion"])
    print("-------------------")