list_string = []

with open("./Input/Letters/starting_letter.txt","r") as fin:
    list_tmp = fin.readlines()
    for x in list_tmp:
        list_string.append(x)

with open("./Input/Names/invited_names.txt","r") as fin:
    list_string2 = fin.readlines()
    for x in list_string2:
        txt = x.strip()
        list_tmp = list_string
        list_tmp[0] = list_tmp[0].replace("[name]",txt)
        letter_name = "letter_for_" + txt
        with open(f"./Output/ReadyToSend/{letter_name}","w") as fout:
            for index in list_tmp:
                fout.write(index)
        list_tmp[0] = list_tmp[0].replace(txt,"[name]")
