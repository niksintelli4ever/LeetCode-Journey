class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dict1=defaultdict(list)
        slist = s.split(" ")
        for i in range(len(slist)):
            dict1[slist[i]].append(i)
        dict2 = defaultdict(list)
        for i in range(len(pattern)):
            dict2[pattern[i]].append(i)
        
        if dict1.values() == dict2.values():
            return True
        list1= []
        for i in dict1.values():
            list1.append(i)
        list2 = []
        for i in dict2.values():
            list2.append(i)
        if list1== list2:
            return True
        return False
        