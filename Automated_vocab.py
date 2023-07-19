#Created this file to automate writing words and their corresponding meanings in  txt file everyday to some extent
# since I had a decicated number of words to learn everyday, the variable n here is not flexible for cases where I have not decided the no of words I am gng to
# learn that day.
#in case of diff paths , use this variable instead of a dedicated path in open()
p = input("Path of the file : ")
n = int(input("enter the no of words : "))
with open(p,"a") as file :
    for _ in range(n) :
        w = input("Word : ")
        m = input("Meaning : ")
        file.write(f"{w} : {m}\n")
