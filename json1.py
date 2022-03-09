import json
objeto_json='{"Nombre":"Fernando","Grupo":"A","Edad":35}'
objeto_py=json.loads(objeto_json)
print("\nJSON datos: ")
print(objeto_py)
print("\nNombre: ",objeto_py["Nombre"])
print("Grupo: ",objeto_py["Grupo"])
print("Edad: ",objeto_py["Edad"])
