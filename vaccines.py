# WHO standard vaccination schedule

WHO_SCHEDULE = [
    {"name": "BCG",         "age_months": 0,   "description": "Protects against Tuberculosis"},
    {"name": "OPV-0",       "age_months": 0,   "description": "Oral Polio Vaccine (birth dose)"},
    {"name": "Hepatitis B", "age_months": 0,   "description": "Protects against Hepatitis B"},
    {"name": "OPV-1",       "age_months": 6,   "description": "Oral Polio Vaccine (1st dose)"},
    {"name": "PCV-1",      "age_months": 6, "description": "Prevents pneumonia"},
    {"name": "DPT-1",       "age_months": 6,   "description": "Diphtheria, Pertussis, Tetanus (1st dose)"},
    {"name": "Rotavirus-1", "age_months": 6, "description": "Prevents severe diarrhea"},
    {"name": "Rotavirus-2", "age_months": 10, "description": "Second dose"},
    {"name": "OPV-2",       "age_months": 10,  "description": "Oral Polio Vaccine (2nd dose)"},
    {"name": "DPT-2",       "age_months": 10,  "description": "Diphtheria, Pertussis, Tetanus (2nd dose)"},
    {"name": "OPV-3",       "age_months": 14,  "description": "Oral Polio Vaccine (3rd dose)"},
    {"name": "DPT-3",       "age_months": 14,  "description": "Diphtheria, Pertussis, Tetanus (3rd dose)"},
    {"name": "PCV-2",     "age_months": 14, "description": "Booster dose"},
    {"name": "MMR",         "age_months": 12,  "description": "Measles, Mumps, Rubella"},
    {"name": "Typhoid",     "age_months": 24,  "description": "Protects against Typhoid fever"},
    {"name": "Hepatitis A", "age_months": 12,  "description": "Protects against Hepatitis A"},
    {"name": "Varicella",   "age_months": 12,  "description": "Protects against Chickenpox"},
    {"name": "DPT-B",       "age_months": 18,  "description": "DPT Booster dose"},
    {"name": "MMR-2",       "age_months": 24,  "description": "MMR second dose"},
]

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
