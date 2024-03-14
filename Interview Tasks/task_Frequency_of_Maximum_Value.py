def frequencyOfMaxValue(numbers, q):

    # SOLUTION 1:
    
    max_number = numbers[len(numbers)-1]
    max_number_list = [1] * len(numbers)
    count = 0
    result = []
    for i in range(len(numbers)-1, -1, -1):
        if numbers[i] > max_number:
            max_number = numbers[i]
            count = 1
        elif numbers[i] == max_number:
            count += 1
        
        max_number_list[i] = count
        # print(max_number_list)

    for i in q:
        result.append(max_number_list[i-1])

    # print(result)
        

    # SOLUTION 2:

    # prev_x = q[0]
    # count_list = []
    
    # for x in q:
    #     if x < prev_x:
    #         prev_x = x
    #         if numbers[x-1] > max_number:
    #             max_number =  numbers[x-1]
    #             count = 1
    #         elif numbers[x-1] == max_number:
    #             count += 1
    #     else:
    #         max_number = max(numbers[x-1:])
    #         count = numbers[x-1:].count(max_number)
    #     count_list.append(count)
    #     count = 0

    # print(count_list)

if __name__ == "__main__":
    # numbers_count = int(input().strip())
    # numbers = []
    # for _ in range(numbers_count):
    #     numbers_item = int(input().strip())
    #     numbers.append(numbers_item)

    # q_count = int(input().strip())
    # q = []
    # for _ in range(q_count):
    #     q_item = int(input().strip())
    #     q.append(q_item)
    numbers = list(map(int, input().strip().split()))
    q = list(map(int, input().strip().split()))

    frequencyOfMaxValue(numbers, q)