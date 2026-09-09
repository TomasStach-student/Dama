def duplicate_count(text):
    text = text.lower()
    videne_znaky = []
    duplikaty = []
    for znak in text:
        if znak in videne_znaky:
            if znak not in duplikaty:
                duplikaty.append(znak)
        else:
            videne_znaky.append(znak)
    return len(duplikaty)

def swap_values(pair: list) -> None:
    pair1=[pair[1], pair[0]]
    return pair1

print(swap_values([51651,16516]))