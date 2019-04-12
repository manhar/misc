import requests

def minimumSwaps(arr):
    #print(arr)
    number_of_swap = 0
    sorted_array =list( arr)
    sorted_array.sort()
    l = len (arr)
    print("Performing swap")
    while arr != sorted_array :
        #print(arr, sorted_array)
        for i in range(l):
            if arr[i] != i+1:
                x = arr[i]
                #print(x)
                arr[i] = arr[x-1]
                arr[x-1] = x
                number_of_swap += 1
                #print(arr)
                break
    return number_of_swap

if __name__ == '__main__':

    test_case8="https://hr-testcases-us-east-1.s3.amazonaws.com/70816/input08.txt?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1554464676&Signature=lidW0uSwQ0rtrzRBen4nzgUKbuI%3D&response-content-type=text%2Fplain"
    test_case14 = "https://hr-testcases-us-east-1.s3.amazonaws.com/70816/input14.txt?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1554466334&Signature=UsjvhNxoTCWHOX6QY8HtXRswqg8%3D&response-content-type=text%2Fplain"

    r = requests.get(test_case14)
    txt = r.text.splitlines()[1]
   # print(txt.split(" "))
    arr = list( int (x) for x in txt.split(" "))
    #print(arr)

    print(minimumSwaps(arr))



