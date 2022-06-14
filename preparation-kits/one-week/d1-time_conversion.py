TWELVE = "12"
MIDNIGHT = "00"
BEFORE_NOON = "AM"
AFTER_NOON = "PM"

def time_conversion(ampm_time):
    military_time, indicator = ampm_time[:-2], ampm_time[-2:]
    hours, minutes, seconds = military_time.split(":")
    
    if indicator == BEFORE_NOON and hours == TWELVE:
            return f"{MIDNIGHT}:{minutes}:{seconds}"
    elif indicator == AFTER_NOON and hours != TWELVE:
            hours = int(hours) + 12
            return f"{hours}:{minutes}:{seconds}"

    return military_time