import os

paramList = [
    ['bicycle', 60_0000],
]

""" 
    ['bicycle', 60_0000],
    ['flowers', 60_0000],
    ['garden', 60_0000],
    ['stump', 60_0000],
    ['treehill', 60_0000],

    ['bonsai', 30_0000],
    ['counter', 30_0000],
    ['kitchen', 30_0000],
    ['room', 30_0000],

    ['drjohnson', 60_0000],
    ['playroom', 30_0000],

    ['train', 30_0000],
    ['truck', 60_0000],
"""

num = 1
for i in range(1, num+1):
    for params in paramList:
        scene = params[0]
        data = 'data/' + scene
        # data = 'data\\' + scene
        final_budget = params[1]
        output = "output/" + scene + "-" + str(i)
        # output = "output\\" + scene + "-" + str(i)

        one_cmd = f'python train.py -s {data} -m {output} --final_budget {final_budget}'
        two_cmd = f'python render.py -m {output} --skip_train'
        three_cmd = f'python metrics.py -m {output}'
        four_cmd = f'python fps.py -m {output}'

        os.system(one_cmd)
        os.system(two_cmd)
        os.system(three_cmd)
        os.system(four_cmd)

