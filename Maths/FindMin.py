def main():
    def findMin(z):
        minNum = z[0]
        for i in z:
            if minNum > i:
                minNum = i
        return minNum

    print(findMin([0,2,4,6,8,10,-8,25,-60])) # = -60

if __name__ == '__main__':
    main()
