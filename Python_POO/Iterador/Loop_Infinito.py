class Meuiterador:
    def __iter__(self):
       return self
    
    def __next__(self):
       raise StopIteration

for i in Meuiterador():
   print(i)

