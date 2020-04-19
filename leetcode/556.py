class Solution:
    def nextGreaterElement(self, n: int) -> int:
        binary = str(n)[::-1]
        i = 1
        while i < len(binary) and binary[i] >= binary[i-1]:
            i += 1
        # 7 2 3 5 4
        # now i points at next small bit -- 3
        if i == len(binary):
            return -1
        j = 0
        while j < len(binary) and binary[j] <= binary[i]:
            j += 1
        # now j points at first bit greater that b[i] -- 4
        # swap b[j:i] & b[j]
        # 7 2 3(i) 5 4(j) --> 7 2 4(j) 3(i) 5
        # i, j == 1, 0 --> b[:0] '' + b[1:2] '1' + b[0] '2' + b[2:] '' ==> b == '12'
        binary = ''.join(sorted(binary[:j]+binary[j+1:i+1])[::-1]) + binary[j] + binary[i+1:]
        res = int(binary[::-1])
        if res >= 2**31:
            return -1
        return res
