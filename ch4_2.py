import random

scores = [random.uniform(30.00, 50.00) for _ in range(5)]
avs = sum(scores)/len(scores)
print('Value random :' ,*[f'{score:.2f}' for score in scores])
print(f'Total value : {sum(scores):.2f}')
print(f'Average value : {avs:.2f}' )
