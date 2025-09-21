def kwarg_dict_builder(name, **kwargs):
    profile = {"name" : name}
    profile.update(kwargs)
    return profile

profile1 = kwarg_dict_builder("Alice", age=25, city="New York", profession="Engineer")

#works even if the positional arg is passed as keyword arg and the order doesnt matter but the name of the key should be the same as the one defined in parameters : "name" in this case
profile2 = kwarg_dict_builder(age=25, name="Alice", city="New York", profession="Engineer")

print(profile1, profile2)