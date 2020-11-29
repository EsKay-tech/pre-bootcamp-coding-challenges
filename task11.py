def common_letters(word_1, word_2):
    output = sorted(''.join(set(word_1).intersection(word_2)))
    common = str(output)[1:-1]
    print("Common letters:", common)


common_letters("home", "hello")
