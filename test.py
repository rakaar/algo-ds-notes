def count_frequency(word_list):
    L = []
    for new_word in word_list:
        print('new_word ', new_word)
        for entry in L:
            if new_word == entry[0]:
                print('if')
                entry[1] = entry[1] + 1
                break
        else:
            print('else')
            L.append([new_word,1])
    return L


print(count_frequency(['the','he','the','a', 'a','a','a','a']))