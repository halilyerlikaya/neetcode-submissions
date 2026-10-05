class Solution:

    def encode(self, strs: List[str]) -> str:
        wordlocs = [0]
        result = ""
        for word in strs: 
            wordlocs.append(wordlocs[-1]+len(word))
            result += word
        wordlocs = str(wordlocs)[:-1]
        print(wordlocs)
        return str(len(wordlocs))+wordlocs+ result        

    def decode(self, s: str) -> List[str]:
        result = []
        wordCount = int(s[0: s.find('[') ]) -1 
        s  = s[s.find('[')+1:]
        print(s)
        wordlocs = s[0:wordCount].split(',')
        s = s[wordCount:]
        wordlocs = [int(x) for x in wordlocs]
        for i in range(len(wordlocs)-1):
            result.append(s[wordlocs[i]:wordlocs[i+1]])
        return result