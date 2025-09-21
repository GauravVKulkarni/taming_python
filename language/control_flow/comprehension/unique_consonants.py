string = "abracadabra"

unique_consonants = {x for x in string if x not in {"a","e","i","o","u"}}

print(unique_consonants)