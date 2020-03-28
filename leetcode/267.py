from collections import Counter
class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        counter = Counter(s)
        center = ""
        for c, v in counter.items():
            if v & 1:
                if center != "":
                    return []
                center = c
            counter[c] //= 2
        #print(counter)
        if center and counter[center] == 0:
            del counter[center]
        def generate_permutation(chars, counter, path, bucket):
            if len(chars) == 0:
                bucket.append(path)
            for idx, c in enumerate(chars):
                counter[c] -= 1
                if counter[c] == 0:
                    generate_permutation(chars[0:idx]+chars[idx+1:], counter, path+c, bucket)
                else:
                    generate_permutation(chars, counter, path+c, bucket)
                counter[c] += 1
        half_palindromes = []
        generate_permutation(''.join(counter.keys()), counter, "", half_palindromes)
        return [s+center+s[::-1] for s in half_palindromes]
        
