def are_anagrams(word1, word2):
    cleaned1 = sorted(word1.replace(" ", "").lower())
    cleaned2 = sorted(word2.replace(" ", "").lower())

    return cleaned1 == cleaned2