class Solution:
    def calPoints(self, operations: List[str]) -> int:
        l = list()
        for op in operations:
            if op == "+":
                v1 = l[-1]
                v2 = l[-2]
                l.append(v1 + v2)
            elif op == "D":
                l.append(l[-1] * 2)
            elif op == "C":
                l.pop()
            else:
                l.append(int(op))

        return sum(l)