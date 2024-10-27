class Solution:
    def decodeString(self, s: str) -> str:
        def decode(s, i):
            result = ""
            while i < len(s) and s[i] != "]":
                if s[i].isdigit():
                    k = ""
                    while i < len(s) and s[i].isdigit():
                        k += s[i]
                        i += 1
                    i += 1
                    k = int(k)
                    output, i = decode(s, i)
                    result += k * output
                    i += 1
                else:
                    result += s[i]
                    i += 1
            return result, i

        result, _ = decode(s, 0)
        return result
