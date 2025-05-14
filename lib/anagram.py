# your code goes here!
class Anagram:
     def __init__(self, target_word):
        self.target_word = target_word

     def match(self, possible_anagrams):
        matches = []
        target = self.target_word.lower()
        sorted_target = sorted(target)

        for word in possible_anagrams:
            candidate = word.lower()
            if candidate != target and sorted(candidate) == sorted(target):
                matches.append(word)
        return matches