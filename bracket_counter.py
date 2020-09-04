def bracket_counter(bracket):
    count = 0
    count1 = 0
    count2 = 0
    for i in range(len(bracket)):
        try:
            if bracket[i] == "(" and (bracket[i + 1] != "}" and bracket[i + 1] != "]"):
                count += 1
            elif bracket[i] == ")":
                if count != 0:
                    count -= 1
                else:
                    return f"{bracket} --> False"
            elif bracket[i] == "{" and (bracket[i + 1] != ")" and bracket[i + 1] != "]"):
                count1 += 1
            elif bracket[i] == "}":
                if count1 != 0:
                    count1 -= 1
                else:
                    return f"{bracket} --> False"
            elif bracket[i] == "[" and (bracket[i + 1] != ")" and bracket[i + 1] != "}"):
                count2 += 1
            elif bracket[i] == "]":
                if count2 != 0:
                    count2 -= 1
                else:
                    return f"{bracket} --> False"
        except Exception as e:
            return f"{bracket} --> False"
    if count == 0 and count1 == 0 and count2 == 0:
        return f"{bracket} --> True"
    else:
        return f"{bracket} --> False"


if __name__ == "__main__":
    try:
        for _ in range(int(input("Enter the number of times to run loop "))):
            print(bracket_counter(input()))
    except Exception as e:
        print(e)
