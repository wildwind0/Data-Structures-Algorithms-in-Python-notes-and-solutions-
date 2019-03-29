

def factoria(n):
    if n==0:
        return 1
    else:
        return n * factoria(n-1)

if __name__ == "__main__":
    print(factoria(4))