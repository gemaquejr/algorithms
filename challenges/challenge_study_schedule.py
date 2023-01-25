def study_schedule(permanence_period, target_time):
    students = 0

    # Ajuda da Maria Carolina na mentoria

    if target_time:
        for login, logout in permanence_period:
            if not type(login) is int or not type(logout) is int:
                return None
            if login <= target_time <= logout:
                students += 1
        return students
    return None
