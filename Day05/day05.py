input = list(open('Day05/input.txt').read().splitlines())

rules = {}
updates = []
rule_parse = True
for line in input:
    if line == '\n' or line == '':
        rule_parse = False
        continue
    if rule_parse:
        pages = []
        first, last = line.split('|')
        if first in rules:
            pages = rules[first]
            pages.append(last)
        else:
            pages.append(last) 
        rules[first] = pages
    else:
        pages = []
        for page in line.split(','):
            pages.append(page)
        updates.append(pages)


part1 = []
part2 = []
for update in updates:
    correct = True
    for i, page in enumerate(update):
        if page not in rules.keys():
            continue
        order = rules[page]
        for ord in order:
            if ord in update and i > update.index(ord):
                correct = False
    if correct:
        part1.append(update[len(update) // 2])
    else:
        fixed = False        
        while(not fixed):
            fixed = True
            update_copy = update
            for i, page in enumerate(update):
                if page not in rules.keys():
                    continue
                order = rules[page]
                for ord in order:
                    if ord not in update:
                        continue
                    ord_index = update.index(ord)
                    if i > ord_index:
                        temp = update[i]
                        update_copy[i] = update[ord_index]
                        update_copy[ord_index] = temp
                        fixed = False
            update = update_copy
        part2.append(update[len(update) // 2])
                

print(sum(list(map(int, part1))))
print(sum(list(map(int, part2))))