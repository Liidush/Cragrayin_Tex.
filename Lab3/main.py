class ListSumWithCarryover:
    def __init__(self, list1, list2):
        if not isinstance(list1, list) or not isinstance(list2, list):
            raise TypeError("Երկու մուտքներն էլ պետք է լինեն 'List' տիպի:")

        if not all(isinstance(i, int) for i in list1) or not all(
            isinstance(i, int) for i in list2
        ):
            raise ValueError("Լիստերի բոլոր տարրերը պետք է լինեն ամբողջ թիվ:")

        self.list1 = list1
        self.list2 = list2
        self.result = []
        self.carry = 0

    def sum_lists(self):
        max_len = max(len(self.list1), len(self.list2))

        self.list1.extend([0] * (max_len - len(self.list1)))
        self.list2.extend([0] * (max_len - len(self.list2)))

        for i in range(max_len):
            total = self.list1[i] + self.list2[i] + self.carry

            self.result.append(total % 10)
            self.carry = total // 10

        if self.carry > 0:
            self.result.append(self.carry)

        return self.result

    def subtract_list(self, result, list_to_subtract):
        carry = 0
        subtracted_result = []

        list_to_subtract.extend([0] * (len(result) - len(list_to_subtract)))

        for i in range(len(result)):
            diff = result[i] - list_to_subtract[i] - carry
            if diff < 0:
                diff += 10
                carry = 1
            else:
                carry = 0

            subtracted_result.append(diff)

        while len(subtracted_result) > 1 and subtracted_result[-1] == 0:
            subtracted_result.pop()

        return subtracted_result


list1 = [9, 9, 9, 9, 9, 9, 9]
list2 = [9, 9, 9, 9]

sum_with_carry = ListSumWithCarryover(list1, list2)
result = sum_with_carry.sum_lists()

print("Արդյունքը:", result)

subtracted_result = sum_with_carry.subtract_list(result, list2)
print("result - list2 =", subtracted_result)
