has_ticket = True
knife_length = 25

if has_ticket:
    if knife_length <= 20:
        print("通过安检")
    else:
        print("安检不通过，刀的长度为%d" % knife_length)
else:
    print("请买票")