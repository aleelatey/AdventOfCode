def main():
    f=open("data.txt", "r")
    data = f.readlines()
    total = 0
    for x in data:
        total += abs(int(x)/3)-2
    print total
if __name__== "__main__":
    main()
 
