def solution(arr1, arr2):
    for i, r in enumerate(arr2):
        arr1[i] = list(map(lambda x, y: x + y, arr1[i], r))
        
    return arr1
   
if __name__=="__main__":
    arr1, arr2 = [[1, 2], [2, 3]], [[3, 4], [5, 6]]
    print(f'arrays: {arr1}, {arr2} | Sol: {solution(arr1, arr2)} | Ans: [[4, 6], [7, 9]]')
    
    arr1, arr2 = [[1], [2]], [[3], [4]]
    print(f'arrays: {arr1}, {arr2} | Sol: {solution(arr1, arr2)} | Ans: [[4], [6]]')
