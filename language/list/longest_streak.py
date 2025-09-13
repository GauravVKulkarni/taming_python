gym_log = [
    "Y","N","Y","Y","Y","N","Y","N","N","Y",
    "Y","Y","N","Y","Y","Y","Y","N","N","Y",
    "N","Y","Y","Y","N","N","Y","Y","Y","Y",
    "Y","N","N","Y","Y","Y","Y","Y","N","Y"
]

curr_streak = 0
max_streak = 0
curr_start = 0
best_start = 0
best_end = 0

for i, item in enumerate(gym_log):
    if item == "Y":
        if curr_streak == 0:
            curr_start = i
        curr_streak += 1
        if curr_streak > max_streak:
            max_streak = curr_streak
            best_start = curr_start
            best_end = i
    elif item == "N":
        curr_streak = 0

print(f"Max streak: {max_streak} from {best_start} to {best_end}")