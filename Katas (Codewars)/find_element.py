def find_element(arr: list, num: int) -> int:
    for element in arr:
        if element == num:
            return num
        elif num not in arr:
            return -1
        
if __name__ == "__main__":
    print(find_element([1, 2, 3], 3))