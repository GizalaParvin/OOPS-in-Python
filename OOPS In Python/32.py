class RemainderCalculator:
    def __init__(self, n, k, a): 
        self.n = n 
        self.k = k 
        self.a = a 
    def calculate_remainders(self): 
        rem = {} 
        for num in self.a: 
            remainder = num % self.k 
            if remainder != 0: 
                if remainder not in rem:
                   rem[remainder] = 1 
                else: 
                    rem[remainder] += 1 
        return rem 
    def find_maximum_result(self, rem): 
        max_moves = 0 
        for r in rem: 
            moves_needed = (rem[r] -1) *self.k + (self.kr) 
            if moves_needed > max_moves: 
                max_moves = moves_needed 
        if max_moves == 0: 
            return max_moves 
        else: 
                return max_moves + 1 
if __name__ == '__main__': 
    from sys import stdin, stdout, setrecursionlimit 
    setrecursionlimit(10**6) 
    t = int(stdin.readline()) 
    for _ in range(t): 
        n, k = map(int, stdin.readline().split()) 
        a = list(map(int, stdin.readline().split())) 
        remainder_calculator = RemainderCalculator (n, k, a) 
        remainders = remainder_calculator.calculate_remainders() 
        result = remainder_calculator.find_maximum_result(remainders) 
        print(result)