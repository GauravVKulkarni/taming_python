user_ids = [
    "u1","u2","u3","u4","u5","u2","u6","u7","u8","u3",
    "u9","u10","u11","u12","u13","u14","u15","u5","u16","u17",
    "u18","u19","u20","u21","u22","u23","u24","u25","u26","u3",
    "u27","u28","u29","u30","u1","u12","u18","u25","u7","u15"
]

id_set = set()
duplicate_ids = set()

for id in user_ids:
    if id not in id_set:
        id_set.add(id)
    else:
        duplicate_ids.add(id)

print(duplicate_ids)