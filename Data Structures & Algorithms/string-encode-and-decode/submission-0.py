class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for word in strs:
            out += str(len(word)) + "#" + word
        return out


    def decode(self, text: str) -> List[str]:
        out = []
        # loop through the sring with two pointers (i,j = 0)
        # i from the length part
        # j until #is seen
        # Copy part of the string from #+1 to lenght of the word (wc)
        # move i to next word by adding wc
        # this address words with #in between (pe#t) & large words above 9 wc
        i = 0
        while i < len(text):
            j = i 
            while text[j] != '#':
                j +=1
            wc = int(text[i : j])
            word = text[j +1 : j+1+wc]
            out.append(word)
            i = j + wc + 1
        return out
