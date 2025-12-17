# Modul untuk fungsi kalkulasi risiko diabetes

def calculate_risk(data):
    """
    Fungsi untuk menghitung skor risiko diabetes.
    Menggunakan loop untuk iterasi faktor risiko dan if-else untuk penilaian.
    Rumus sederhana: BMI + faktor usia + riwayat keluarga + aktivitas.
    Skor maksimal 100, berdasarkan WHO/CDC inspirasi.
    """
    # Hitung BMI
    height_m = data['height'] / 100
    bmi = data['weight'] / (height_m ** 2)
    
    # Skor awal berdasarkan BMI
    score = 0
    if bmi < 18.5:
        score += 10  # Risiko rendah tapi mungkin malnutrisi
    elif 18.5 <= bmi < 25:
        score += 20
    elif 25 <= bmi < 30:
        score += 40
    else:
        score += 60
    
    # Loop untuk faktor tambahan (looping buatan)
    factors = [
        ('age', data['age']),
        ('family_history', 1 if data['family_history'] == 'Ya' else 0),
        ('activity_level', {'Rendah': 20, 'Sedang': 10, 'Tinggi': 0}[data['activity_level']])
    ]
    
    for factor_name, value in factors:  # Looping
        if factor_name == 'age':
            if value > 45:  # If buatan
                score += 20
            elif value > 30:
                score += 10
        elif factor_name == 'family_history':
            if value == 1:  # If buatan
                score += 15
        elif factor_name == 'activity_level':
            score += value  # Tambah langsung
    
    # Pastikan skor tidak melebihi 100
    return min(score, 100)

def risk_category(score):
    """
    Fungsi untuk kategori risiko menggunakan if-else.
    """
    if score < 30:  # If buatan
        return "Rendah"
    elif 30 <= score < 60:
        return "Sedang"
    else:
        return "Tinggi"