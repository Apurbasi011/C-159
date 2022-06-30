dictionary = {"fruit" : "mango",
              "colour" : "pink",
              "bird" : "sparrow"}

try:
    print(dictionary["animal"])
    
except(KeyError):
    print("Key Animal Is Not Present In The Dictionary")
