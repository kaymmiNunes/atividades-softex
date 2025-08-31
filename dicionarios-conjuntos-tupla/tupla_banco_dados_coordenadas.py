# Verificador de pontos turísticos por coordenadas

pontos_turisticos = {
    (-22.95169865170328, -43.21050865767194): "Cristo Redentor - Rio de Janeiro",
    (-12.974205546315755, -38.513053557671945): "Elevador Lacerda - Salvador",
    (-7.225581660905272, -35.88009090052937): "Açude Velho - Campina Grande"
}

# Entrada do usuário
lat = float(input("Digite a latitude: "))
lon = float(input("Digite a longitude: "))

# Procura aproximada
encontrado = False
for (plat, plon), nome in pontos_turisticos.items():
    if round(lat, 5) == round(plat, 5) and round(lon, 5) == round(plon, 5):
        print(f"Local encontrado: {nome}")
        encontrado = True
        break

if not encontrado:
    print("Local não encontrado.")
