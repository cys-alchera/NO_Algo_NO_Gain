class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counter = 0
        for word in words:
            temp_counter = 0
            new_chars = chars
            for string in word:
                if string in new_chars:
                    new_chars = new_chars.replace(string, '',1)
                    temp_counter += 1
                else:
                    break
                
                if temp_counter == len(word):
                    counter += temp_counter
        return counter
