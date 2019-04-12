from collections import  Counter
def parseSQL():

    f=open("testSQL.txt", "r")
    for line in f:
        print (line)
    print("Parser")


def anagram_check (s1, s2):
    res = Counter(s1) == Counter(s2)
    print(res)
    return  res


def anagram_test(s1, s2):
    s1_len =len(s1)
    s2_len = len(s2)

    s1_dict={}
    s2_dict={}

    if s1_len != s2_len:
        return False

    for index, s1_char in enumerate(s1):

        #s1_char = s1[index]
        s2_char = s2[index]

        if s1_char in s1_dict:
            s1_dict[s1_char] = s1_dict[s1_char]+1
        else:
            s1_dict[s1_char] = 1

        if s2_char in s2_dict:
            s2_dict[s2_char] = s2_dict[s2_char] + 1
        else:
            s2_dict[s2_char] = 1

    if s1_dict == s2_dict:
        return True
    else:
        return False


print(str(anagram_test("aba", "baac")))

#anagram_check("aba", "baaa")