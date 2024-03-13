import heapq

def minSum(num, k):
    num = [-x for x in num]
    heapq.heapify(num)

    for _ in range(k):
        element = -heapq.heappop(num)
        new_element = (element + 1) // 2
        heapq.heappush(num, -new_element)

    print(-sum(num))

if __name__ == "__main__":
    num = map(int, input().rstrip().split())
    k = int(input())
    minSum(num, k)
