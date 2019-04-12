
def reverse(x):
    string_length = len(x)
    word = ""  #initialize container to store each word in the senetence
    result = "" # initinalise container to store final output
    for index in range(string_length):
        print(index, string_length-1, x[index])
        if x[index] == " " or index == string_length-1:
            if index == string_length-1:
                word += x[index]
            for i in range(len(word)-1, -1, -1):
               ## print(word[i])

                result += word[i]

            word = ""
            result += " "

        else:
            #print(word)
            word += x[index]
    #print("Final Result")
    return result





print(reverse(""))

