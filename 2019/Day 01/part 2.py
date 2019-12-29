def main():
    f=open("data.txt", "r")
    data = f.readlines()
    total = 0
    for x in data:
        fuel = max(abs(int(x)/3)-2,0)
        j = fuel
        while j > 0:
            k = max(abs(int(j)/3)-2,0)
            fuel += k
            j = k
        total += fuel
    print total
if __name__== "__main__":
    main()
