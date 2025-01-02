# A ideia desses códigos é fazer uma calculadora de medidas de comprimento. 
print()
print("Olá, bem-vindo. Vamos Converter suas Medidas de Comprimento? ") 
print()
print("Para melhor compreensão, sempre digite suas respostas com letras minúsculas!")
print()
print("Opções > km: Quilômetro | hm: Hectômetro | dam: Decâmetro | m: Metro")
print("Opções > dm: Decímetro | cm: Centímetro | mm: Milímetro")
print()
Pergunta_um = (input("Insira qual Unidade você tem: "))
Pergunta_dois = float(input("Insira o valor dessa unidade: "))
Pergunta_tres = (input("Para qual Unidade você gostaria de mudar? "))

# Maior para o Menor:
if Pergunta_um == "km" and Pergunta_tres == "hm":
    resposta_um = Pergunta_dois * 10
    print(f"A medida em Hectômetros é: {resposta_um:.2f}")

if Pergunta_um == "hm" and Pergunta_tres == "dam":
    resposta_dois = Pergunta_dois * 10
    print(f"A medida em Decâmetros é: {resposta_dois:.2f}")

if Pergunta_um == "dam" and Pergunta_tres == "m":
    resposta_tres = Pergunta_dois * 10
    print(f"A medida em Metros é: {resposta_tres:.2f}")

if Pergunta_um == "m" and Pergunta_tres == "dm":
    resposta_quatro = Pergunta_dois * 10
    print(f"A medida em Decímetros é: {resposta_quatro:.2f}")

if Pergunta_um == "dm" and Pergunta_tres == "cm":
    resposta_cinco = Pergunta_dois * 10
    print(f"A medida em Centímetros é: {resposta_cinco:.2f}")

if Pergunta_um == "cm" and Pergunta_tres == "mm":
    resposta_seis = Pergunta_dois * 10
    print(f"A medida em Milímetros é: {resposta_seis:.2f}")

# Quilômetros: 
if Pergunta_um == "km" and Pergunta_tres == "dam":
    resposta_sete = Pergunta_dois * 100
    print(f"A medida em Decâmetros é: {resposta_sete:.2f}")

if Pergunta_um == "km" and Pergunta_tres == "m":
    resposta_oito = Pergunta_dois * 1000
    print(f"A medida em Metros é: {resposta_oito:.2f}")

if Pergunta_um == "km" and Pergunta_tres == "dm":
    resposta_nove = Pergunta_dois * 10000
    print(f"A medida em Decímetros é: {resposta_nove:.2f}")

if Pergunta_um == "km" and Pergunta_tres == "cm":
    resposta_dez = Pergunta_dois * 100000
    print(f"A medida em Centímetros é: {resposta_dez:.2f}")

if Pergunta_um == "km" and Pergunta_tres == "mm":
    resposta_onze = Pergunta_dois * 1000000
    print(f"A medida em Milímetros é: {resposta_onze:.2f}")

# Hectômetro: 
if Pergunta_um == "hm" and Pergunta_tres == "m":
    resposta_doze = Pergunta_dois * 100
    print(f"A medida em Metros é: {resposta_doze:.2f}")

if Pergunta_um == "hm" and Pergunta_tres == "dm":
    resposta_treze = Pergunta_dois * 1000
    print(f"A medida em Decímetros é: {resposta_treze:.2f}")

if Pergunta_um == "hm" and Pergunta_tres == "cm":
    resposta_quatorze = Pergunta_dois * 10000
    print(f"A medida em Centímetros é: {resposta_quatorze:.2f}")

if Pergunta_um == "hm" and Pergunta_tres == "mm":
    resposta_quinze = Pergunta_dois * 100000
    print(f"A medida em Milímetros é: {resposta_quinze:.2f}")

# Decâmetro: 
if Pergunta_um == "dam" and Pergunta_tres == "dm":
    resposta_dezesseis = Pergunta_dois * 100
    print(f"A medida em Decímetros é: {resposta_dezesseis:.2f}")

if Pergunta_um == "dam" and Pergunta_tres == "cm":
    resposta_dezessete = Pergunta_dois * 1000
    print(f"A medida em Centímetros é: {resposta_dezessete:.2f}")

if Pergunta_um == "dam" and Pergunta_tres == "mm":
    resposta_dezoito = Pergunta_dois * 10000
    print(f"A medida em Milímetros é: {resposta_dezoito:.2f}")

# Metro: 
if Pergunta_um == "m" and Pergunta_tres == "cm":
    resposta_dezenove = Pergunta_dois * 100
    print(f"A medida em Centímetros é: {resposta_dezenove:.2f}")

if Pergunta_um == "m" and Pergunta_tres == "mm":
    resposta_vinte = Pergunta_dois * 1000
    print(f"A medida em Milímetros é: {resposta_vinte:.2f}")

# Decímetro: 
if Pergunta_um == "dm" and Pergunta_tres == "mm":
    resposta_vinteum = Pergunta_dois * 100
    print(f"A medida em Milímetros é: {resposta_vinteum:.2f}")

# Menor para Maior: 
if Pergunta_um == "mm" and Pergunta_tres == "cm":
    resposta_vinte_dois = Pergunta_dois / 10
    print(f"A medida em Centímetros é: {resposta_vinte_dois:.2f}")

if Pergunta_um == "cm" and Pergunta_tres == "dm":
    resposta_vinte_tres = Pergunta_dois / 10
    print(f"A medida em Decímetros é: {resposta_vinte_tres:.2f}")

if Pergunta_um == "dm" and Pergunta_tres == "m":
    resposta_vinte_quatro = Pergunta_dois / 10
    print(f"A medida em Metros é: {resposta_vinte_quatro:.2f}")

if Pergunta_um == "m" and Pergunta_tres == "dam":
    resposta_vinte_cinco = Pergunta_dois / 10
    print(f"A medida em Decâmetros é: {resposta_vinte_cinco:.2f}")

if Pergunta_um == "dam" and Pergunta_tres == "hm":
    resposta_vinte_seis = Pergunta_dois / 10
    print(f"A medida em Hectômetros é: {resposta_vinte_seis:.2f}")

if Pergunta_um == "hm" and Pergunta_tres == "km":
    resposta_vinte_sete = Pergunta_dois / 10
    print(f"A medida em Quilômetros é: {resposta_vinte_sete:.2f}")

# Milímetros: 
if Pergunta_um == "mm" and Pergunta_tres == "dm":
    resposta_vinte_oito = Pergunta_dois / 100
    print(f"A medida em Decímetros é: {resposta_vinte_oito:.2f}")

if Pergunta_um == "mm" and Pergunta_tres == "m":
    resposta_vinte_nove = Pergunta_dois / 1000
    print(f"A medida em Metros é: {resposta_vinte_nove:.2f}")

if Pergunta_um == "mm" and Pergunta_tres == "dam":
    resposta_trinta = Pergunta_dois / 10000
    print(f"A medida em Decâmetros é: {resposta_trinta:.5f}")

if Pergunta_um == "mm" and Pergunta_tres == "hm":
    resposta_trinta_um = Pergunta_dois / 100000
    print(f"A medida em Hectômetros é: {resposta_trinta_um:.6f}")

if Pergunta_um == "mm" and Pergunta_tres == "km":
    resposta_trinta_dois = Pergunta_dois / 1000000
    print(f"A medida em Quilômetros é: {resposta_trinta_dois:.7f}")

# Centímetros:
if Pergunta_um == "cm" and Pergunta_tres == "m":
    resposta_trinta_tres = Pergunta_dois / 100
    print(f"A medida em Metros é: {resposta_trinta_tres:.2f}")

if Pergunta_um == "cm" and Pergunta_tres == "dam":
    resposta_trinta_quatro = Pergunta_dois / 1000
    print(f"A medida em Decâmetros é: {resposta_trinta_quatro:.2f}")

if Pergunta_um == "cm" and Pergunta_tres == "hm":
    resposta_trinta_cinco = Pergunta_dois / 10000
    print(f"A medida em Hectômetros é: {resposta_trinta_cinco:.2f}")

if Pergunta_um == "cm" and Pergunta_tres == "km":
    resposta_trinta_seis = Pergunta_dois / 100000
    print(f"A medida em Quilômetros é: {resposta_trinta_seis:.2f}")

# Decímetros:
if Pergunta_um == "dm" and Pergunta_tres == "dam":
    resposta_trinta_sete = Pergunta_dois / 100
    print(f"A medida em Decâmetros é: {resposta_trinta_sete:.2f}")

if Pergunta_um == "dm" and Pergunta_tres == "hm":
    resposta_trinta_oito = Pergunta_dois / 1000
    print(f"A medida em Hectômetros é: {resposta_trinta_oito:.2f}")

if Pergunta_um == "dm" and Pergunta_tres == "km":
    resposta_trinta_nove = Pergunta_dois / 10000
    print(f"A medida em Quilômetros é: {resposta_trinta_nove:.2f}")

# Decâmetros:
if Pergunta_um == "dam" and Pergunta_tres == "km":
    resposta_quarenta = Pergunta_dois / 100
    print(f"A medida em Quilômetros é: {resposta_quarenta:.2f}")