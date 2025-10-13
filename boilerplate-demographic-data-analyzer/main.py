from demographic_data_analyzer import calculate_demographic_data

resultados = calculate_demographic_data()

for clave, valor in resultados.items():
    print(f"{clave}:\n{valor}\n")