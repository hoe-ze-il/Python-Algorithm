from HashTable import HashTable

N, M = map(int, input().split())
hashTable = HashTable(M)
for i in range(N):
    book = input()
    key = sum(map(ord, book))
    hashTable.put(key, book)
for key in range(M):
    print(key, ", ".join(hashTable.get(key)))