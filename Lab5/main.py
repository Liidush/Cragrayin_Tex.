from collections import Counter

class AnagramChecker:
    def are_anagrams(self, s: str, t: str) -> bool:
        list_s = list(s)
        list_t = list(t)

        print(f"List for string '{s}': {list_s} (ID: {id(list_s)})")
        print(f"List for string '{t}': {list_t} (ID: {id(list_t)})")

        return Counter(list_s) == Counter(list_t)

    def check_anagrams(self):
        s = input("Enter the first string (s): ")
        t = input("Enter the second string (t): ")

        if self.are_anagrams(s, t):
            print(f'"{s}" and "{t}" are anagrams.')
        else:
            print(f'"{s}" and "{t}" are not anagrams.')


checker = AnagramChecker()
checker.check_anagrams()
