import re
from math import floor, prod
import gmpy2 as gmpy

class Monkey:
    def __init__(self,items,operation,test,throw_true,throw_false,monkeys) -> None:
        self.items = [gmpy.mpz(x) for x in items]
        self.inspect = lambda old: eval(operation)
        self.test = lambda item_value: item_value%test==0
        self.throw_true = throw_true
        self.throw_false = throw_false
        self.monkeys = monkeys
        self.has_inspected = 0
    
    def round(self):
        for item in self.items:
            # Adjust worry value
            worry = self.inspect(item)
            self.has_inspected += 1
            # Monkey is bored, decrease worry level
            if part==1:
                worry = floor(worry/3)
            # Test and throw to next monkey
            if self.test(worry):
                monkeys[self.throw_true].items.append(worry)
            else:
                monkeys[self.throw_false].items.append(worry)
        self.items.clear()

    def add_item(self,item):
        self.items.append(worry)

    def __str__(self):
        return str(self.items)

myfile = 'test.txt'
monkeys = list()

with open(myfile, 'r') as file:
    data = file.read().split('\n\n')

while data:
    if data[0].split()[0] == "Monkey":
        items = [int(x) for x in re.findall('[0-9]+',data[0].split('\n')[1])]
        operation = data[0].split('=')[1].split('\n')[0]
        test,true_to,false_to =[int(x) for x in re.findall('[0-9]+',data[0].split('Test')[1])]
        new_monkey = Monkey(items,operation,test,true_to,false_to,monkeys)
        monkeys.append(new_monkey)
        data.pop(0)

part = 1
for _ in range(20):
    for monkey in monkeys:
        # print(monkey)
        monkey.round()

insp = [x.has_inspected for x in monkeys]
insp.sort()
print('Inspected: ',insp, ' Product:', prod(insp[-2:]))

part = 2
for r in range(2000):
    print("Round: ", r)
    for monkey in monkeys:
        monkey.round()

insp = [x.has_inspected for x in monkeys]
insp.sort()
print('Inspected: ',insp, ' Product:', prod(insp[-2:]))