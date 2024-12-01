"""
Group Anagrams

Problem: Given an array of strings, group anagrams together. Return a list of lists
where each inner list contains strings that are anagrams of each other.

An anagram is a word formed by rearranging the letters of another word.
For example, "cinema" and "iceman" are anagrams.

Example 1:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat","tea","ate"], ["tan","nat"], ["bat"]]

Example 2:
Input: [""]
Output: [[""]]

Example 3:
Input: ["a"]
Output: [["a"]]
"""

"""
Approach:
["top", "pot", "pit", "sip", "tip"]

i = 3
result = [["top", "pot"], ["pit"]]

dict = {"top": []}
dict = {"top": ["pot"]}
dict = {"pit": [],"top": ["pot"]}
dict = {"sip": ["tip"], "pit": [], "top": ["pot"]}


Approach 2
["top", "pot", "pit", "sip", "tip"]

{top, pot}, {pit}, {sip, tip}

agrams = [set1: [], set2: []]
"""

agrams = {}

def addAgram(str):
    strAsSet = set(str),
    for key, value in agrams:
        if key-strAsSet == {}:
            value.add(str)
            return
    agrams[strAsSet] = [str]


def groupAnagrams(strs):
    for entry in strs:
        addAgram(entry)
    return [agrams[k] for k in agrams.keys]


# Test cases
def test_group_anagrams():
    # Test case 1: Basic anagrams
    assert sorted(
        map(sorted, groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    ) == sorted(
        [sorted(["eat", "tea", "ate"]), sorted(["tan", "nat"]), sorted(["bat"])]
    )

    # Test case 2: Empty string
    assert groupAnagrams([""]) == [[""]]

    # Test case 3: Single character
    assert groupAnagrams(["a"]) == [["a"]]

    # Test case 4: No anagrams
    assert sorted(map(sorted, groupAnagrams(["cat", "dog", "pig"]))) == sorted(
        [["cat"], ["dog"], ["pig"]]
    )

    print("All test cases passed!")


if __name__ == "__main__":
    test_group_anagrams()
