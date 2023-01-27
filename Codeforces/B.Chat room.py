s = input()
h_index = s.find("h")
if h_index != -1:
    s = s[h_index+1:]
    e_index = s.find("e")
    if e_index != -1:
        s = s[e_index + 1:]
        l_index1 = s.find("l")
        if l_index1 != -1:
            s = s[l_index1 + 1:]
            l_index2 = s.find("l")
            if l_index2 != -1:
                s = s[l_index2 + 1:]
                o_index = s.find("o")
                if o_index != -1:
                    print("YES")
                else:
                    print("NO")
            else:
                print("NO")
        else:
            print("NO")
    else:
        print("NO")
else:
    print("NO")
