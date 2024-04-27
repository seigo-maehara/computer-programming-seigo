input_stirng = input().split(",")
i = input_stirng.index("boundary")
inokashira_list = input_stirng[:i]
inokashira_express_list = input_stirng[i+1:]
inokasira_nonex_list = []
for j in range(len(inokashira_list)):
    if inokashira_list[j] not in inokashira_express_list:
        inokasira_nonex_list.append(inokashira_list[j])
print(inokasira_nonex_list)