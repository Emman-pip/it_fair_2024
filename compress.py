def compress(chars: list[str]) -> int:
    temp = 0
    count = 0
    finalArr = []
    for i in range(len(chars)):
        if i == 0:
            finalArr.append(chars[i])
            temp = i
            count += 1
            continue
        elif chars[i] != chars[temp] or i == len(chars) - 1:
            print(chars[i], temp, chars[temp], chars[i] == chars[temp])
            print(count)
            if count > 1:
                for v in str(count):
                    finalArr.append(v)
            count = 1
            temp = i
            if i != len(chars) - 1:
                finalArr.append(chars[i])
        count += 1

    return len(finalArr)


print(compress(["a"]))


