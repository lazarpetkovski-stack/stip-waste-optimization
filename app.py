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
