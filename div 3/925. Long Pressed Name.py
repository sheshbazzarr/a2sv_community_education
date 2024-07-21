class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name_pointer = 0
        typed_pointer = 0

        while typed_pointer < len(typed):
            if name_pointer < len(name) and name[name_pointer] == typed[typed_pointer]:
                name_pointer += 1
            elif typed_pointer == 0 or typed[typed_pointer] != typed[typed_pointer - 1]:
                return False
            typed_pointer += 1

        return name_pointer == len(name)

# july 21,2024
