def recommend(symptoms_text):
    symptoms = symptoms_text.lower().split(',')

    db = {
        'fever': ['Paracetamol', 'Crocin'],
        'cold': ['Cetirizine', 'Sinarest'],
        'cough': ['Benadryl', 'Dextromethorphan'],
        'headache': ['Paracetamol', 'Ibuprofen'],
        'stomach pain': ['Cyclopam', 'Buscopan'],
        'vomiting': ['Ondansetron'],
        'diarrhea': ['ORS', 'Loperamide'],
        'allergy': ['Cetirizine', 'Levocetirizine'],
        'body pain': ['Voveran', 'Brufen']
    }

    medicines = set()

    for s in symptoms:
        s = s.strip()
        if s in db:
            medicines.update(db[s])

    if not medicines:
        return ['No matching medicines found. Consult doctor']

    return list(medicines)
