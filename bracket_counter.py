def bracket_counter(bracket):
    count = 0
    count1 = 0
    count2 = 0
    for char in bracket:
        if char == "(":
            count += 1
        elif char == ")":
            if count != 0:
                count -= 1
            else:
                return f"{bracket} --> False"
        if char == "{":
            count1 += 1
        elif char == "}":
            if count1 != 0:
                count1 -= 1
            else:
                return f"{bracket} --> False"
        if char == "[":
            count2 += 1
        elif char == "]":
            if count2 != 0:
                count2 -= 1
            else:
                return f"{bracket} --> False"
    if count == 0 and count1 == 0 and count2 == 0:
        return f"{bracket} --> True"
    else:
        return f"{bracket} --> False"


if __name__ == "__main__":
    for _ in range(int(input("Enter the number of times to run loop "))):
        print(bracket_counter(input()))
