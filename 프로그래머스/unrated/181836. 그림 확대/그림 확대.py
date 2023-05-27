def solution(picture, k):
    rows = len(picture)
    cols = len(picture[0])
    new_rows = rows * k
    new_cols = cols * k

    new_picture = [['.'] * new_cols for _ in range(new_rows)]

    for i in range(rows):
        for j in range(cols):
            pixel = picture[i][j]
            for x in range(i * k, (i + 1) * k):
                for y in range(j * k, (j + 1) * k):
                    new_picture[x][y] = pixel

    return [''.join(row) for row in new_picture]