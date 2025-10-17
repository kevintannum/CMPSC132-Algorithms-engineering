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
