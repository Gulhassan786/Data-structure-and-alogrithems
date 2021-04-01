
t_cases = int(input("Enter taset cases: "))
count = 0
for k in range(0, t_cases):
    lis = []
    no_element = int(input("Enter elements number: "))
    for i in range(0, no_element):
        lis.append(int(input("Enter element of the list: ")))

    for i in range(1, (len(lis)-1)):
        for j in range((i+1), (len(lis))):

            if lis[0] > lis[i]:
                lis[0], lis[j] = lis[j], lis[0]
                count += 2
            elif lis[j] < lis[i]:
                lis[i], lis[j] = lis[j], lis[i]
                count += 2
    print(lis, count)
