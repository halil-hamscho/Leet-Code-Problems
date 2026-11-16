"""


Follow
- followee: follower
- can we store that in a Hashmap?
we probably need some type of lookp 

edge case where we follow, they post then we unfollow, and we getnews
- we should not return anything from that user

We also need something to have priority since we need it to be ordered from most recent to least recent

hashmap for follow relationships
priority queue for generic news?
- we can have an logic statement that 

are tweets IDs guranteed to increase chronologically, or are they arbitrary unique identifiers?
- Tweet IDs are unique, but they are not guranteed to be in chronological order


Invariant:

The heap contains at most one tweet from each relevant user at a time, not every tweet they've posted

Pattern: K Way Merge using a heap

1. the heap drives the algorithm
rather than storing all tweets in a heap or simply iterating throguh it, we're actively using 
- heappop()
- heappush()
to determine which tweet to process next

Time: O(F + K log F)
Space: O(F + K)
F relevant number of users
K = feed size

User 1: [1, 4, 7]  ←
User 2: [2, 5, 8]  ←
User 3: [3, 6, 9]  ←

Heap initially: [9, 8, 7]

Pop 9 → Move User 3's pointer backward → Push 6
Pop 8 → Move User 2's pointer backward → Push 5
Pop 7 → Move User 1's pointer backward → Push 4

Problem Involving:
    1. Multiple individually sorted collections
    2. A requirement to combine or retrieve elements in sorted order
    3. A desire to avoid processing every element

Consider whether a heap can maintain one candidate from each collection


"""
import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.hashmap = defaultdict(set)
        self.timestamp = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:

        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1
        
    def getNewsFeed(self, userId: int) -> list[int]:
        """
        Uses heap to retrieve them in chronological order
        - the heap contains the most recent unprocessed tweet from each relevant user who still has tweets remaining
        """
        max_heap = []

        users = self.following[userId] | {userId}

        for user in users:
            user_tweets = self.tweets[user]
            if not user_tweets:
                continue

            index = len(user_tweets) - 1
            timestamp, tweet = user_tweets[index]

            max_heap.append((-timestamp, user, index, tweet))

        heapq.heapify(max_heap)

        feed = []
        while max_heap and len(feed) < 10:
            _, user, index, tweet = heapq.heappop(max_heap)
            feed.append(tweet)

            if index > 0:
                previous_index = index - 1
                previous_timestamp, previous_tweet = self.tweets[user][previous_index]

                heapq.heappush(
                    max_heap, 
                    (-previous_timestamp, user, previous_index, previous_tweet))

        return feed 


    def follow(self, followerId: int, followeeId: int) -> None:
        self.hashmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.hashmap[followerId]:
            self.hashmap[followerId].remove(followeeId)
        
if __name__ == "__main__":
    twitter = Twitter()

    twitter.postTweet(1, 5)
    twitter.postTweet(1, 1000)
    twitter.postTweet(1, 1001)
    twitter.postTweet(1, 3)
    twitter.postTweet(1, 101)
    twitter.postTweet(1, 13)
    twitter.postTweet(1, 10)
    twitter.postTweet(1, 2)
    twitter.postTweet(1, 94)
    twitter.postTweet(1, 505)
    twitter.postTweet(1, 333)

    result = twitter.getNewsFeed(1)

    print("Actual:", result)
    print("Expected:", [333, 505, 94, 2, 10, 13, 101, 3, 5])