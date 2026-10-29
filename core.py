
def calc_total_intake(mass, ref_intake):
    try:
        mass=float(mass)
        ref_intake = float(ref_intake)
        total_intake = mass * ref_intake / 100
        total_intake = str(round(total_intake, 1))
    except ValueError:
        total_intake = "Erreur"

    return total_intake


def calc_mass_to_eat(ref_intake, total_intake):
    try:
        ref_intake = float(ref_intake)
        total_intake = float(total_intake)
        mass = total_intake * 100 / ref_intake
        mass = str(round(mass, 0))
    except ValueError:
        mass = "Erreur"
    except ZeroDivisionError:
        mass = "Erreur"
    return mass
