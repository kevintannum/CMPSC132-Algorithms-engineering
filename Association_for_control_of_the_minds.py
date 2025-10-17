N = int(input())

recipes = []
for _ in range(N):
    parts = list(map(int, input().split()))
    k, ing = parts[0], parts[1:]
    recipes.append(ing)

used = set() # ingredients that are already in some cauldron


# Union-Find using hash maps
ingredients_cauldron = {}  #tells you which ingredient is in which cauldron
size = {}    # amount of ingredients in cauldron

answer = 0

def make_set(x):
    if x not in ingredients_cauldron:
        ingredients_cauldron[x] = x
        size[x] = 1

def find(x): ## find which cauldron has which ingredients (part of union find)
    if x not in ingredients_cauldron:
        make_set(x)
    
    if ingredients_cauldron[x] != x:
        ingredients_cauldron[x] = find(ingredients_cauldron[x]) #Finn rekursivt 
    return ingredients_cauldron[x]


def union(a, b):
    cauldron_a, cauldron_b = find(a), find(b)
    if cauldron_a == cauldron_b:
        return
    if size[cauldron_a] < size[cauldron_b]:
        cauldron_a, cauldron_b = cauldron_b, cauldron_a
    ingredients_cauldron[cauldron_b] = cauldron_a
    size[cauldron_a] += size[cauldron_b]




for S in recipes:
    # count members of each cauldron 
    count = {}
    for ingredient in S:
        if ingredient in used:
            root = find(ingredient)            # check which cauldron the ingredient is in
            count[root] = count.get(root, 0) + 1     

    # check all neighbours of every ingredient in their cauldron 
    can_pour_cauldron = True
    for root, present_count in count.items():
        full_size = size[find(root)]          # number of ingredients in that cauldron
        if present_count != full_size:        
            can_pour_cauldron = False
            break

    if not can_pour_cauldron:
        continue                
    
    answer += 1
    
    make_set(S[0]) 
    for ingredient in S[1:]:
        make_set(ingredient)      # Ensure each ingredient exists
        union(S[0], ingredient)   # Connect it to the first ingredient

    used.update(S)

print(answer)