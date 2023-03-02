k=int(input("enter string length"))
str = "Wangoes technology pvt ltd vijay nagar indore"
string = []
text = str.split(" ")

for x in text:
    if len(x) > k:
        string.append(x)
print(string)

