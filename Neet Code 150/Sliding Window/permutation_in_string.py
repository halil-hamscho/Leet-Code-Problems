
'''

- Make Frequency Map
- Get Window Size

- Make 2nd Map
Iterate through s2
    For every new R pointer value
    - Insert into 2nd Map
    Once r >= window size
        delete the left most value
        l += 1 (this will help us continue the sliding window)
    once we delete
    we check if they are the same

    "Draggingly Checking"
    Delete left most value that makes the window too big, then check if they are the same
    

'''


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap = {}
        # make our frequency map
        for char in s1:
            hashmap[char] = 1 + hashmap.get(char, 0)

        # this is how big we want the window
        window_size = len(s1) 
        
        l = 0
        hashmap_2 = {}
        #Move right pointer 
        for r in range(len(s2)):
            # Insert s2[r] into the hashmap
            hashmap_2[s2[r]] = 1 + hashmap_2.get(s2[r],0)

            if r >= window_size:
                if hashmap_2[s2[l]] == 1:
                    del hashmap_2[s2[l]]
                else:
                    hashmap_2[s2[l]] -= 1
                l += 1

            if hashmap == hashmap_2: 
                return True
        return False

def main():
    print()
    s1 = "adc"
    s2 = "dcda"
    test = Solution()
    print(test.checkInclusion(s1,s2))

if __name__ == "__main__":
    main()
