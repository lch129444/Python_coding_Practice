names = ["Joey Tribbiani", "Monica Geller"]
usernames = []
for name in names:
    usernames.append(name.lower().replace(" ","-"))
print(usernames)
