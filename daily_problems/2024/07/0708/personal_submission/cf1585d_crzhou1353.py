class Fenwick:
    def __init__(self, n: int):
        self.tree = [0] * (n + 1)
    
    def add(self, i: int) -> None:
        i += 1
        while i < len(self.tree):
            self.tree[i] += 1
            i += i & -i
        
    def pre(self, i: int) -> int:
        i += 1
        result = 0
        while i > 0:
            result += self.tree[i]
            i -= i & -i
        return result

data = input().split()
t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = int(data[index])
    nums = list(map(int, data[index + 1: index + 1 + n]))
    index += 1 + n
    cnt = [0] * (n + 1)
    a = 0
    for num in nums:
        if cnt[num]:
            a = 1
            break
        cnt[num] += 1
    if a == 1:
        results.append("YES")
        continue
    
    fen = Fenwick(n)
    cnt = 0
    # 判断奇偶即可
    for i in range(n - 1, -1, -1):
        cnt ^= fen.pre(nums[i] - 1) & 1
        fen.add(nums[i])
    if cnt == 0:
        results.append("YES")
    else:
        results.append("NO")

stdout.write("\n".join(results))
