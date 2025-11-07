def main():
    int_var = 7
    float_var = 5.3
    str_var = "welcome"
    list_var = [1, 2, 3]
    tpl_var = (4, 5, 6)
    dict_var = {"name": "lucy", "age": 34}
    set_var = {4, 5, 6}
    bool_var = False

    # printing all
    print("Initial Values")
    print(f"Integer: {int_var}")
    print(f"Float: {float_var}")
    print(f"String: {str_var}")
    print(f"List: {list_var}")
    print(f"Tuple: {tpl_var}")
    print(f"Dictionary: {dict_var}")
    print(f"Set: {set_var}")
    print(f"Boolean: {bool_var}")
    print("-" * 50)

    # numeric operations
    sum_num = int_var + float_var
    power_num = int_var ** 2
    div_num = int_var / 2
    print("Numeric Operations")
    print(f"Sum = {sum_num}")
    print(f"Power = {power_num}")
    print(f"Division = {div_num}")
    print("-" * 50)

    # string operations
    new_str = str_var + " to record"
    sub_str = new_str[3:10]
    print("String Operations")
    print(f"New String = {new_str}")
    print(f"Substring (3:10) = {sub_str}")
    print(f"Uppercase = {new_str.upper()}")
    print("-" * 50)

    # list operations
    list_var.append(4)
    list_var.remove(2)
    print("List Operations")
    print(f"After append & remove: {list_var}")
    print(f"Second element: {list_var[1]}")
    print(f"Length of list: {len(list_var)}")
    print("-" * 50)

    # tuple operations
    a, b, c = tpl_var
    print("Tuple Operations")
    print(f"Tuple: {tpl_var}")
    print(f"Unpacked values: {a}, {b}, {c}")
    print(f"Access element 2: {tpl_var[1]}")
    print("-" * 50)

    # dictionary operations
    dict_var["city"] = "Mumbai"
    dict_var["age"] = 35
    print("Dictionary Operations")
    print(f"Updated Dictionary: {dict_var}")
    print(f"Keys: {list(dict_var.keys())}")
    print(f"Values: {list(dict_var.values())}")
    print("-" * 50)

    # set operations
    set_var.add(7)
    set_var.discard(4)
    print("Set Operations")
    print(f"After add & remove: {set_var}")
    print(f"Union with {{5,8}}: {set_var | {5, 8}}")
    print(f"Intersection with {{5,8}}: {set_var & {5, 8}}")
    print("-" * 50)

    # boolean operations
    and_res = bool_var and False
    or_res = bool_var or True
    not_res = not bool_var
    print("Boolean Operations")
    print(f"AND = {and_res}")
    print(f"OR = {or_res}")
    print(f"NOT = {not_res}")

    print("\n✅ Program executed successfully!")


if __name__ == '__main__':
    main()
