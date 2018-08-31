import numpy as np

def removing_padding(img_np, value):
    mask = img_np == value
    print(mask)
    # delete upper row
    row = 0
    while np.all(mask[row]) == True:
        # 0 is for aways delete 1'st row of new np_img
        # axis = 0 is for row wise delete
        img_np = np.delete(img_np, 0, axis = 0) 
        row += 1
    print(img_np)
    # delete lower row
    row = mask.shape[0] - 1 # start from last row 
    while np.all(mask[row]) == True:
        # -1 is for aways delete last row of new np_img
        # axis = 0 is for row wise delete
        img_np = np.delete(img_np, -1, axis = 0) 
        row -= 1
    print(img_np)
    # delete left column
    col = 0
    while np.all(mask[:,col]) == True:
        # 0 is for aways delete 1st column of new img_np
        # axis = 1 is for column wise delete
        img_np = np.delete(img_np, 0, axis = 1)
        col += 1
    print(img_np)
    # delete right column
    col = mask.shape[1] - 1
    while np.all(mask[:,col]) == True:
        # -1 is for aways delete last column of new img_np
        # axis 1 is for column wise delte
        img_np = np.delete(img_np, -1, axis = 1)
        col -= 1
    print(img_np)

    return img_np

if __name__ == '__main__':
    # img_np = np.array([[10, 10, 10, 10], 
    #                     [10, 3, 3, 10], 
    #                     [10, 3, 4, 10],
    #                     [10, 10, 10, 10]])
    img_np = np.array([[10, 10, 10, 10, 10, 10, 10],
                        [10, 10, 10, 10, 10, 10, 10], 
                        [10, 10, 30, 10, 30, 10, 10],
                        [10, 10, 10, 10, 10, 10, 10], 
                        [10, 10, 30, 10, 40, 10, 10],
                        [10, 10, 10, 10, 10, 10, 10],
                        [10, 10, 10, 10, 10, 10, 10]])
    print('padd less img', removing_padding(img_np, 10))
    '''
    Out:
    [[30 10 30]
     [10 10 10]
     [30 10 40]]
    '''
    
