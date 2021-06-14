import pandas as pd
from loguru import logger

DATASET_LIMIT = 5

def getDataset(path):
    df = pd.read_excel(path, engine='openpyxl')
    for column in df.columns:
        if 'Unnamed' in column:
            df.drop(column, inplace=True, axis=1) 
    return df[:DATASET_LIMIT]

def collectVertex(df):
    sources = df['src']
    destinations = df['dst']
    vertexes = list(set(list(sources) + list(destinations)))
    vertexes.sort()
    return vertexes

def makeMatrix(vertexes, df):
    matrix = []
    for source in vertexes:
        row = []
        for destination in vertexes:
            if (source != destination):
                status = 'no'
                #logger.debug(destination)
                for index in range(len(df)):
                    if (str(list(set(df.iloc[[index]]['src']))[0]) == source) and (str(list(set(df.iloc[[index]]['dst']))[0]) == destination):
                        #print('yes!')
                        status = 'yes'
                        data = int(df.iloc[[index]]['summ'])
                if status == 'yes': row.append(data)
                if status == 'no': row.append(0)
            else:
                #print('skip')
                row.append(0)
        matrix.append(row)
    return matrix
            

def getConnectablePoints(matrix, vertex, size):
    connectablePoints = []
    index = 0
    for col in range(size):
        if matrix[vertex][col] != 0:
            connectablePoints.append(index)
        index += 1
    return connectablePoints

def defineZeroLevel(matrix, size, iteration):
    zero_checker = True
    for row in range(size):
        if matrix[row][iteration] != 0:
            zero_checker = False
    return zero_checker


def initDefineLevel(matrix, vertexes):
    levelMatrix = []
    for vertex in range(len(vertexes)):
        row = {}
        if defineZeroLevel(matrix, len(vertexes), vertex):
            row = {
                'vertex': vertexes[vertex],
                'level': 1,
                'razrez': []
            }
        else:
            row = {
                'vertex': vertexes[vertex],
                'level': 0,
                'razrez': []
            }
        levelMatrix.append(row)

    return levelMatrix


def defineLevel(matrix, vertexes):
    levelMatrix = initDefineLevel(matrix, vertexes)
    attendedMatrix = []
    for vertex in range(len(vertexes)):
        attendedPoints = []
        attendedMatrix.append(attendedPoints)

    for vertex in range(len(vertexes)):
        if levelMatrix[vertex]['level'] > 0:
            connectablePoints = getConnectablePoints(matrix, vertex, len(vertexes))
            for point in connectablePoints:
                if point not in attendedMatrix[vertex]:
                    
                    levelMatrix[point]['level'] = levelMatrix[vertex]['level'] + 1
                    levelMatrix[point]['razrez'].append({
                        'vertex': vertexes[vertex],
                        'level': levelMatrix[vertex]['level'],
                        'sum': matrix[vertex][point]
                    })

                    attendedMatrix[vertex].append(point)

    return levelMatrix
