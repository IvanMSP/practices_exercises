# The email_list function receives a dictionary, which contains domain names as keys,
# and a list of users as values. Develop a script to generate a list that
# contains complete email addresses (e.g. diana.prince@gmail.com).

#Dictionary
dict_emails = {
    "gmail.com": ["clark.kent", "diana.prince", "peter.parker"],
    "hello.yahoo.com": ["barbara.gordon", "jean.grey"],
    "expandit.hotmail.com": ["bruce.wayne"],
}

def get_mails(dict_emails: dict) -> list:
    emails = list()
    new_emails = {k: [f'{i}@{k}' for i in v] for (k , v) in dict_emails.items()}
    {k: [emails.append(i) for i in v] for k, v in new_emails.items()}
    return emails
# 1 Implement and run test cases for your function


mails = get_mails(dict_emails)
print(mails)