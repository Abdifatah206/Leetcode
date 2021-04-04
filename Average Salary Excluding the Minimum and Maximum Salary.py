class Solution:
    def average(self, salary: List[int]) -> float:
        min1 = min(salary)
        max1 = max(salary)
        lst = []
        lst.append(min1)
        lst.append(max1)
        lst1 = []
        for i in salary:
            if i not  in lst:
                lst1.append(i)
        avg = sum(lst1) / len(lst1)
        return avg