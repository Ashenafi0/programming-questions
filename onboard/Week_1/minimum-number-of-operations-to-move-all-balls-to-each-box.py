class Solution(object):
    def minOperations(self, boxes):
        n = len(boxes)
        answer = [0] * n
        balls = [i for i, box in enumerate(boxes) if box == '1']
        for i in range(n):
            answer[i] = sum(abs(i - j) for j in balls)

        return answer
