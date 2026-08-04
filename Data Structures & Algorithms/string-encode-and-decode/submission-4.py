class Solution:
    # encode the string by including the length of the string followed by a hash so that in decoding we can easily retrieve the length
    # decode the string by extracting the length of each word and append the word to a resulting array

    def encode(self, strs: List[str]) -> str:
        encode_val = ""

        for string in strs:
            encode_val += str(len(string))
            encode_val += "#"
            encode_val += string
        return encode_val

    def decode(self, s: str) -> List[str]:
        i=0
        res=[]

        length_encode = len(s)

        while i < length_encode:
            j=i
            while s[j] != "#":
                j+=1
            
            word_length = int(s[i:j])

            j+=1
            word = s[j:j+word_length]

            i = j + word_length
            res.append(word)
        return res




