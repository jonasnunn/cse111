


provinces_file = open('provinces.txt', 'r')

province_list = []
for province in provinces_file:
    clean_province = province.strip()
    province_list.append(clean_province)

provinces_file.close()

print(province_list)

province_list.pop(0)
province_list.pop()



for i in range(len(province_list)):
    if province_list[i] == "AB":
        province_list[i] = 'Alberta'

count = 0
for province in province_list:
    if province == "Alberta":
        count += 1



print(f'Alberta occures {count} times in the list.')