class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        count = Counter(hand)
        for i in hand:
            if count[i] == 0:
                continue
            for x in range(i, i +groupSize):
                if count[x] ==0:
                    return False
                count[x] -= 1
        return True        