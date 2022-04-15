def main():
	n = int(input())
	print(a(n))
def a(i):
    for j in range(2,i):
        if i % j == 0:
            return "NO"
    return "YES"
if __name__ == "__main__":
    main()