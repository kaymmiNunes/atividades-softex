pontos_turisticos = {
    (-22.95169865170328, -43.21050865767194): "Cristo Redentor - Rio de Janeiro",
    (-12.974205546315755, -38.513053557671945): "Elevador Lacerda - Salvador",
    (-7.225581660905272, -35.88009090052937): "Açude Velho - Campina Grande"
}

coordenada = (float(input("Digite a latitude: ")), float(input("Digite a longitude: ")))

if coordenada in round(pontos_turisticos):
    print(f"Local encontrado: {pontos_turisticos[coordenada]}")
else:
    print("Local não encontrado.")

if