from loguru import logger

from core import (
    collectVertex,
    getDataset,
    makeMatrix,
    defineLevel
)

def outputTable(matrix, vertexes):
    df = getDataset('my set.xlsx')
    vertexes = collectVertex(df)
    matrix, size = makeMatrix(vertexes, df), len(vertexes)
    levelMatrix = defineLevel(matrix, vertexes)

    for vertex in range(size):


# df = getDataset('test local dataset.xlsx')
# df = getDataset('my set.xlsx')
# vertexes = collectVertex(df)
# matrix, size = makeMatrix(vertexes, df), len(vertexes)
# levelMatrix = defineLevel(matrix, vertexes)

# logger.info(f'\n { df }')

# print('\n')

# for vertex in vertexes:
#     logger.debug(vertex)

# print('\n')

# for row in range(size):
#     logger.warning(matrix[row])

# print('\n')

# print('---------------------------------------------------------\n')

# for row in range(size):
#     logger.success(levelMatrix[row]['vertex'])
#     logger.success(f"Level - { levelMatrix[row]['level'] }")
#     #logger.success(levelMatrix[row]['razrez'])

#     print('\n')
    
#     balance = 0

#     if len(levelMatrix[row]['razrez']) > 0:
#         for vertex in levelMatrix[row]['razrez']:
#             balance += vertex['sum'] 
            
#             logger.warning(vertex['vertex'])
#             logger.warning(f"Level - { vertex['level'] }")
#             logger.warning(vertex['sum'])

#             print('\n')
#     else:
#         logger.warning('No points')

#         print('\n')

#     if balance > 0:

#         logger.success(f'Balance - { balance }')
#     print('---------------------------------------------------------')
# #print(len(collectVertex(df)))
