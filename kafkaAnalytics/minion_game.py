#/usr/bin/python3

def count(string, word):
    counter=0
    word_length = len(word)
    for index, value  in enumerate(string):
        print(string[index:word_length + index])
        if string[index:word_length + index] == word:
            counter += 1
    return counter


def calculate_score(string):
    '''
    Given a list, the minion game score is calculated for from the list
    '''
    previous_sequence = ''
    score =0
    for v in string:
        previous_sequence += v  # remebers the previous substring
        score += string.count(previous_sequence)
        print(previous_sequence, string.count(previous_sequence))
    return score



def minion_game(s):
    # your code goes here s=s.up per()
    stuart_score = 0  # s  ore holder for stuart
    kevin_score = 0  # s  ore holder for kevin

    vowels="AEIOU"
    string_length = len(s)

    if 0 < len(s) <= 10e6 :
        previous = ''
        seen = set()  # s  t to remember letters already seen in the string
        for index,v in enumerate(s):
            if v not in seen:
                #seen.add(v)
                print(str(index),v)
                if v in vowels:
                    kevin_score += calculate_score(s[index:string_length])
                else:
                    stuart_score += calculate_score(s[index:string_length])



    print ("Stuart " + str(stuart_score))
    print("Kevin "+ str(kevin_score))


if __name__ == '__main__':
    # s = input()
    minion_game("BAANANAS")
    #print(count("banana", "ana"))