"""
Every evening villagers in a small village gather around a big fire and sing songs.
A prominent member of the community is the bard. Every evening, if the bard is present, he sings a brand new song that no villager has heard before, and no other song is sung that night. In the event that the bard is not present, other villagers sing without him and exchange all songs that they know.

Given the list of villagers present for consecutive evenings, output all villagers that know all songs sung during that period.

Input
The first line of input contains an integer, the number of villagers. The villagers are numbered 1 to N. Villager number 1
 is the bard.

The second line contains an integer the number of evenings.

The next lines contain the list of villagers present on each of the 
 evenings. Each line begins with a positive integer the number of villagers present that evening, followed by 
 N positive integers separated by spaces representing the villagers.

No villager will appear twice in one night and the bard will appear at least once across all nights.

Output all villagers that know all songs, including the bard, one integer per line in ascending order.
"""


V = int(input())
E = int(input())


total_songs = 0
known_songs = [set() for i in range(V)]

evenings = [] 
for i in range(E):
    present = list(map(int, input().split()))
    evenings.append(present)
    

for present in evenings:
    k = present[0]
    attendees = present[1:1+k]
    if 1 in attendees:
        total_songs +=1
        new_song = total_songs
        for v in attendees:
            known_songs[v-1].add(new_song)
    else:
        collectively_known = set()
        for v in attendees:
            collectively_known |= known_songs[v - 1]
        for v in attendees:
            known_songs[v - 1] = set(collectively_known)


for v in range(1, V + 1):
    if len(known_songs[v - 1]) == total_songs:
        print(v)

