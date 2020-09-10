import random
body_parts = ['глаза', 'руки', 'ноги', 'волосы', 'пальцы']
characteristic = ['большие', 'отвратительные', 'грязные', 'длинные', 'вонючие']

a = random.choice(body_parts)
b = random.choice(characteristic)

print('Привет, старнник! Как тебя зовут?')
name = input()
print('%s, ты знаешь, куда ты попал? Это страна дурацких дразнилок!'%(name))
print('Твои', a, 'такие', b, '!')
