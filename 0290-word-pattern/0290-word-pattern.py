class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dict1=defaultdict(set)
        dict2=defaultdict(set)
        list1=[]
        list2=[]
        slist=s.split(" ")

        for i in range(len(slist)):
            dict1[slist[i]].add(i)

        for i in range(len(pattern)):
            dict2[pattern[i]].add(i)

        for i in dict1.values():
            list1.append(i)

        for i in dict2.values():
            list2.append(i)

        if list1== list2:
            return True

        return False