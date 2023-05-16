if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(arr)
    first_score = max(arr)
    secound_score = min(arr)
    for i in range(len(arr)):
        if arr[i]>secound_score and arr[i] != first_score:
            secound_score = arr[i]

    print(secound_score)
