#!/usr/bin/python


def fun(s):
    # return True if s is a valid email, else return False
    valid_username = "abcdefghijklmnopqrstuvwxyz1234567890_-"
    valid_website = "abcdefghijklmnopqrstuvwxyz1234567890"
    if s.count("@") != 1 :
        return False
    else:

        username, trailer = s.split("@")
        website = trailer.split(".")[0]
        extension = trailer.split(".")[-1]

        # print(username, website, extension)

        if not (set(valid_username).issuperset(set(username))) or username == "":
            # print("username check failed")
            return False
        else:
            if not (set(valid_website).issuperset(set(website))) or website == "":
                # print("website checked failed")
                return False
            else:
                if not (1 <= len(extension) <= 3):
                    # print("extension check failed", extension)
                    return False
                else:
                    # print(s)
                    return True


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)