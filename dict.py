# name = "yogesh is the god boy and yogEsh and Yogesh is the friend of yogesh"

# nulll = 0

# count = name.lower().count("yogesh")
# print(count)

# names = ["yogesh Kumar", "yogesh singh", "rahul sharma", "yogesh and friends", "anita"]
# total = sum(name.lower().count("yogesh") for name in names)
# print(total)

# seven = [7, 4, 6, 7, 8, 3]
# eight = [7]

# if (7 in seven):
#     print("yes")
    
# else:
#     print("not")
    
# inputt = input("what's your wrold name?")
# print(inputt)

code_input = input("enter the http status code: ")

try:
    code = int(code_input)
except ValueError:
    print("Please enter a valid integer HTTP status code.")
    raise SystemExit(1)

def http_status(code):
    return {
        200: "ok",
        404: "not found",
        400: "bad request",
        500: "internal server error",
    }.get(code, "unknown status code")

print(http_status(code))