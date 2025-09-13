roll_numbers = [
    "U1001","U1002","U1003","U1005","U1006","U1007",          # U1004 missing
    "U1009","U1010","U1011","U1012","U1013","U1014",          # U1008 missing
    "U1016","U1017","U1018","U1019","U1020",                  # U1015 missing
    "U1022","U1023","U1024","U1025","U1026","U1027",          # U1021 missing
    "U1030","U1031","U1032","U1033","U1034","U1035",          # U1028,U1029 missing
    "U1037","U1038","U1039","U1040","U1041","U1042","U1043",  # U1036 missing
    "U1045","U1046","U1047","U1048","U1049","U1050",          # U1044 missing
    "U1052","U1053","U1054","U1055","U1056",                  # U1051 missing
    "U1058","U1059","U1060"                                   # U1057 missing
]

def extract_missing_ranges(roll_numbers_list, prefix_length):

    prefix = roll_numbers_list[0][0:prefix_length]
    int_roll_numbers = []

    for num in roll_numbers_list:
        int_roll_numbers.append(int(num[prefix_length:]))

    int_roll_numbers = sorted(list(set(int_roll_numbers)))

    missing_roll_numbers = []

    for i, num in enumerate(int_roll_numbers):
        if i != 0 and num > int_roll_numbers[i-1] + 1:
            if num > int_roll_numbers[i-1] + 2:
                missing_roll_numbers.append(f"{prefix}{int_roll_numbers[i-1]+1}-{prefix}{num-1}")
            else:
                missing_roll_numbers.append(f"{prefix}{num-1}")


    return missing_roll_numbers

print(extract_missing_ranges(roll_numbers, 1))