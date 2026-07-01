import itertools

print("=============================================")
print("   ЈП ИСАР - ШТИП: ЛОГИСТИЧКА ОПТИМИЗАЦИЈА   ")
print("=============================================\n")

# 1. ДЕФИНИРАЊЕ НА ЛОКАЦИИТЕ И МАТРИЦАТА НА РАСТОЈАНИЈА (во километри)
# Ова се реални/проценети растојанија меѓу точките во Штип
distanci = {
    ("Baza", "Senjak"): 2.5,
    ("Baza", "Babi"): 4.0,
    ("Baza", "Deponija"): 12.0,
    
    ("Senjak", "Babi"): 3.0,
    ("Senjak", "Deponija"): 11.0,
    ("Senjak", "Baza"): 2.5,
    
    ("Babi", "Senjak"): 3.0,
    ("Babi", "Deponija"): 14.0,
    ("Babi", "Baza"): 4.0,
    
    ("Deponija", "Baza"): 12.0,
    ("Deponija", "Senjak"): 11.0,
    ("Deponija", "Babi"): 14.0
}

# Населби кои камионот МОРА да ги посети денес
naselbi_za_poseta = ["Senjak", "Babi"]

print("--- АНАЛИЗА НА НАЈКРАТКА РУТА ---")
print("Камионот тргнува од БАЗА, ги собира Сењак и Баби, па носи во ДЕПОНИЈА.\n")

najkrata_ruta = None
najmalku_kilometri = float('inf')

# Со помош на математика ги проверуваме сите можни комбинации (патеки)
# Комбинација 1: База -> Сењак -> Баби -> Депонија
# Комбинација 2: База -> Баби -> Сењак -> Депонија
za_proverka = list(itertools.permutations(naselbi_za_poseta))

for patek in za_proverka:
    # Секогаш почнуваме од База
    trenutna_ruta = ["Baza"] + list(patek) + ["Deponija"]
    
    # Пресметка на вкупната километража за оваа патека
    vkupno_km = 0
    for i in range(len(trenutna_ruta) - 1):
        tocka_A = trenutna_ruta[i]
        tocka_B = trenutna_ruta[i+1]
        vkupno_km += distanci[(tocka_A, tocka_B)]
        
    print(f"Опција: {' -> '.join(trenutna_ruta)} | Вкупно: {vkupno_km} км")
    
    # Проверка дали оваа рута е најдобра досега
    if vkupno_km < najmalku_kilometri:
        najmalku_kilometri = vkupno_km
        najkrata_ruta = trenutna_ruta

print("\n---------------------------------------------")
print("🏆 ОПТИМАЛНО РЕШЕНИЕ ОД СОФТВЕРОТ:")
print(f" -> Најдобра рута: {' -> '.join(najkrata_ruta)}")
print(f" -> Минимална километража: {najmalku_kilometri} км")

# Пресметка на заштеда на гориво (ако камионот троши 25 литри на 100км)
potroseno_gorivo = (najmalku_kilometri / 100) * 25
print(f" -> Проценета потрошувачка на нафта: {potroseno_gorivo:.2f} литри")
print("=============================================")