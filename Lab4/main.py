def isValid(s: str) -> bool:
    stack = []
    bracket_map = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in bracket_map:
            top_element = stack.pop() if stack else "#"
            print(f"Փակագիծ '{char}', վերջինը '{top_element}'")
            if bracket_map[char] != top_element:
                print("Սխալ փակագծեր:")
                return False
        elif char in bracket_map.values():
            stack.append(char)
            print(f"Բաց փակագիծ '{char}' ավելացված:")

    print(f"stack-ի երկարությունը՝ {len(stack)}")
    return len(stack) == 0


user_input = input("Խնդրում եմ մուտքագրեք փակագծերով մի շարք: ")
if isValid(user_input):
    print("Մուտքագրված շարքը ճիշտ է:")
else:
    print("Մուտքագրված շարքը սխալ է:")
