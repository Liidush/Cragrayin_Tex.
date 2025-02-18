input_array = []

input_data = input("Մուտքագրեք թվերը: ")

try:
    input_array = list(map(int, input_data.split(',')))
except ValueError:
    print(" մուտքագրեք ամբողջ թվեր։")
    exit()

sorted_array = sorted(input_array)
print("Սորտավորված զանգվածը՝", sorted_array)

indices_to_check = [0, 3, 5]
duplicates = []

for index in indices_to_check:
    if index < len(sorted_array): 
        element = sorted_array[index]

        if (index > 0 and element == sorted_array[index - 1]) or \
            (index < len(sorted_array) - 1 and element == sorted_array[index + 1]):
            if element not in duplicates:  
                duplicates.append(element)

if duplicates:
    print("Կրկնվող տարրեր՝", duplicates)
else:
    print("Նշված ինդեքսներում կրկնվող տարրեր չկան։")
assert len(duplicates) != 0
