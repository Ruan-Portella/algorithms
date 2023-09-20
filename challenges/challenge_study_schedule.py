def study_schedule(permanence_period, target_time):
    try:
        periods = 0
        if target_time is None:
            return None
        for i in permanence_period:
            if i[0] <= target_time <= i[1]:
                periods += 1
        return periods
    except (IndexError, TypeError, ValueError, AttributeError):
        return None
