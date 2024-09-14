def secondDiagAvg(arr, i, j):
    if i == 0:
        return arr[i][j]/len(arr);

    return arr[i][j]/len(arr) + secondDiagAvg(arr, i-1, j+1)


def main():
    a = [[1,2,3,4],[4,3,2,1],[9,8,7,6],[6,7,8,9]]
    avg = secondDiagAvg(a, len(a)-1, 0)

    print(avg)


if __name__ == "__main__":
    main()