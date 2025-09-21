web_logs = [
    ("u1", "home"), ("u2", "about"), ("u1", "products"), ("u3", "home"),
    ("u2", "contact"), ("u1", "home"), ("u3", "products"), ("u2", "home"),
    ("u1", "about"), ("u4", "home"), ("u4", "products"), ("u3", "contact"),
    ("u2", "products"), ("u4", "about"), ("u1", "contact"), ("u3", "about"),
    ("u4", "contact"), ("u2", "home"), ("u3", "products"), ("u1", "faq"),
    ("u4", "faq"), ("u3", "faq")
]

logs_dict = dict()

for user, page in web_logs:
    if user not in logs_dict:
        logs_dict[user] = {page,}
    else:
        logs_dict[user].add(page)

max_activity = ["", 0]

for i in logs_dict:
    if len(logs_dict[i]) > max_activity[1]:
        max_activity = i, len(logs_dict[i])

print(logs_dict)
print(f"{max_activity[0]} has the most activity of {max_activity[1]} unique webpage access")