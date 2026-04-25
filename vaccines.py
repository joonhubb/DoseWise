WHO_SCHEDULE = [
    
    {"name": "BCG",           "age_months": 0,   "description": "Protects against Tuberculosis"},
    {"name": "OPV-0",         "age_months": 0,   "description": "Oral Polio Vaccine (birth dose)"},
    {"name": "Hepatitis B",   "age_months": 0,   "description": "Protects against Hepatitis B (birth dose)"},
    {"name": "OPV-1",         "age_months": 2,   "description": "Oral Polio Vaccine (1st dose)"},
    {"name": "PCV-1",         "age_months": 2,   "description": "Pneumococcal vaccine — prevents pneumonia (1st dose)"},
    {"name": "DPT-1",         "age_months": 2,   "description": "Diphtheria, Pertussis, Tetanus (1st dose)"},
    {"name": "Rotavirus-1",   "age_months": 2,   "description": "Prevents severe rotavirus diarrhea (1st dose)"},
    {"name": "Hib-1",         "age_months": 2,   "description": "Haemophilus influenzae type b — prevents meningitis (1st dose)"},
    {"name": "OPV-2",         "age_months": 3,   "description": "Oral Polio Vaccine (2nd dose)"},
    {"name": "DPT-2",         "age_months": 3,   "description": "Diphtheria, Pertussis, Tetanus (2nd dose)"},
    {"name": "PCV-2",         "age_months": 3,   "description": "Pneumococcal vaccine (2nd dose)"},
    {"name": "Rotavirus-2",   "age_months": 3,   "description": "Prevents severe rotavirus diarrhea (2nd dose)"},
    {"name": "Hib-2",         "age_months": 3,   "description": "Haemophilus influenzae type b (2nd dose)"},
    {"name": "OPV-3",         "age_months": 4,   "description": "Oral Polio Vaccine (3rd dose)"},
    {"name": "DPT-3",         "age_months": 4,   "description": "Diphtheria, Pertussis, Tetanus (3rd dose)"},
    {"name": "PCV-3",         "age_months": 4,   "description": "Pneumococcal vaccine (3rd dose)"},
    {"name": "IPV",           "age_months": 4,   "description": "Inactivated Polio Vaccine — stronger polio protection"},
    {"name": "Hib-3",         "age_months": 4,   "description": "Haemophilus influenzae type b (3rd dose)"},
    {"name": "Hepatitis B-2", "age_months": 6,   "description": "Hepatitis B (2nd dose)"},
    {"name": "Influenza-1",   "age_months": 6,   "description": "Flu vaccine (1st dose — give annually after this)"},
    {"name": "Measles-1",     "age_months": 9,   "description": "Measles vaccine (1st dose)"},
    {"name": "Vitamin A",     "age_months": 9,   "description": "Prevents blindness and boosts immunity"},
    {"name": "Meningococcal", "age_months": 9,   "description": "Protects against bacterial meningitis"},
    {"name": "MMR",           "age_months": 12,  "description": "Measles, Mumps, Rubella (1st dose)"},
    {"name": "Hepatitis A",   "age_months": 12,  "description": "Protects against Hepatitis A (1st dose)"},
    {"name": "Varicella",     "age_months": 12,  "description": "Protects against Chickenpox (1st dose)"},
    {"name": "PCV-B",         "age_months": 12,  "description": "Pneumococcal booster dose"},
    {"name": "DPT-B",         "age_months": 18,  "description": "DPT Booster dose"},
    {"name": "Hepatitis A-2", "age_months": 18,  "description": "Hepatitis A (2nd dose)"},
    {"name": "Varicella-2",   "age_months": 18,  "description": "Chickenpox 2nd dose"},
    {"name": "Hib-B",         "age_months": 18,  "description": "Hib booster dose"},
    {"name": "MMR-2",         "age_months": 24,  "description": "Measles, Mumps, Rubella (2nd dose)"},
    {"name": "Typhoid",       "age_months": 24,  "description": "Protects against Typhoid fever"},
    {"name": "Hepatitis B-3", "age_months": 24,  "description": "Hepatitis B (3rd dose booster)"},
    {"name": "DPT-2B",        "age_months": 48,  "description": "DPT 2nd booster (4 years)"},
    {"name": "OPV-B",         "age_months": 48,  "description": "Oral Polio booster (4 years)"},
    {"name": "MMR-3",         "age_months": 60,  "description": "MMR booster (5 years)"},
    {"name": "Varicella-3",   "age_months": 60,  "description": "Chickenpox booster (5 years)"},
    {"name": "Tdap",          "age_months": 120, "description": "Tetanus, Diphtheria, Pertussis booster (10 years)"},
    {"name": "HPV-1",         "age_months": 120, "description": "Human Papillomavirus vaccine (1st dose — 10 years)"},
    {"name": "HPV-2",         "age_months": 126, "description": "Human Papillomavirus vaccine (2nd dose — 6 months after 1st)"},
    {"name": "Meningococcal-B","age_months": 132,"description": "Meningococcal booster (11 years)"},
    {"name": "Td-Booster",    "age_months": 180, "description": "Tetanus & Diphtheria booster (15 years)"},
    {"name": "HPV-3",         "age_months": 180, "description": "HPV 3rd dose if not completed earlier (15 years)"},
]

# Risk levels for overdue vaccines
RISK_LEVELS = {
    "BCG":           {"level": "high",   "reason": "TB can be fatal in infants"},
    "OPV-0":         {"level": "high",   "reason": "Polio can cause permanent paralysis"},
    "OPV-1":         {"level": "high",   "reason": "Polio can cause permanent paralysis"},
    "OPV-2":         {"level": "high",   "reason": "Polio can cause permanent paralysis"},
    "OPV-3":         {"level": "high",   "reason": "Polio can cause permanent paralysis"},
    "Hepatitis B":   {"level": "high",   "reason": "Can cause liver failure if untreated"},
    "DPT-1":         {"level": "high",   "reason": "Whooping cough is fatal in infants"},
    "DPT-2":         {"level": "high",   "reason": "Whooping cough is fatal in infants"},
    "DPT-3":         {"level": "high",   "reason": "Whooping cough is fatal in infants"},
    "DPT-B":         {"level": "medium", "reason": "Protection weakens without booster"},
    "MMR":           {"level": "high",   "reason": "Measles kills 100,000+ children yearly"},
    "MMR-2":         {"level": "medium", "reason": "Booster ensures full protection"},
    "Rotavirus-1":   {"level": "medium", "reason": "Leading cause of child diarrhea deaths"},
    "Rotavirus-2":   {"level": "medium", "reason": "Leading cause of child diarrhea deaths"},
    "PCV-1":         {"level": "high",   "reason": "Pneumonia is a top killer of children"},
    "PCV-2":         {"level": "high",   "reason": "Pneumonia is a top killer of children"},
    "PCV-3":         {"level": "medium", "reason": "Booster strengthens protection"},
    "IPV":           {"level": "high",   "reason": "Polio can cause permanent paralysis"},
    "Hib-1":         {"level": "high",   "reason": "Can cause bacterial meningitis"},
    "Hib-2":         {"level": "high",   "reason": "Can cause bacterial meningitis"},
    "Hib-3":         {"level": "medium", "reason": "Booster ensures full protection"},
    "Typhoid":       {"level": "medium", "reason": "Typhoid spreads quickly in communities"},
    "Hepatitis A":   {"level": "medium", "reason": "Liver infection, spreads through food/water"},
    "Varicella":     {"level": "low",    "reason": "Chickenpox can cause complications"},
    "Vitamin A":     {"level": "medium", "reason": "Deficiency causes blindness in children"},
    "Meningococcal": {"level": "high",   "reason": "Bacterial meningitis can be fatal within 24hrs"},
    "HPV-1":         {"level": "medium", "reason": "HPV causes cervical cancer"},
    "HPV-2":         {"level": "medium", "reason": "HPV causes cervical cancer"},
    "Tdap":          {"level": "medium", "reason": "Tetanus protection weakens over time"},
}

def get_schedule(age_months, vaccines_received):
     
    done = []
    overdue = []
    upcoming = []

    for vaccine in WHO_SCHEDULE:
        name = vaccine["name"]
        due_age = vaccine["age_months"]
        description = vaccine["description"]

        if name.lower() in [v.lower() for v in vaccines_received]:
            # Parent said this vaccine was already given
            done.append({
                "name": name,
                "description": description,
                "due_age": due_age
            })
        elif due_age <= age_months:
            # Should have been given by now but wasn't
            overdue.append({
                "name": name,
                "description": description,
                "due_age": due_age,
                "overdue_by": age_months - due_age
            })
        elif due_age <= age_months:
             risk = RISK_LEVELS.get(name, {"level": "medium", "reason": "Consult your doctor"})
             overdue.append({
         "name": name,
         "description": description,
         "due_age": due_age,
         "overdue_by": age_months - due_age,
         "risk_level": risk["level"],
         "risk_reason": risk["reason"]
            })
        else:
            # Not due yet — upcoming
            upcoming.append({
                "name": name,
                "description": description,
                "due_age": due_age,
                "months_away": due_age - age_months
            })
        

    # Sort upcoming by how soon they are due
    upcoming.sort(key=lambda x: x["months_away"])

    return done, overdue, upcoming
