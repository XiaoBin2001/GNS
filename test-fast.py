import os

paramList = [
    ['bicycle', 60_0000, 0.005],
]

"""
    ['bicycle', 60_0000, 0.005],
    ['flowers', 30_0000, 0.005],
    ['garden', 60_0000, 0.005],
    ['stump', 30_0000, 0.005],
    ['treehill', 30_0000, 0.005],

    ['bonsai', 30_0000, 0.02],
    ['counter', 30_0000, 0.02],
    ['kitchen', 30_0000, 0.02],
    ['room', 30_0000, 0.02],

    ['drjohnson', 30_0000, 0.0025],
    ['playroom', 30_0000, 0.0025],

    ['train', 30_0000, 0.02],
    ['truck', 30_0000, 0.02],
"""

num = 1
for i in range(1, num+1):
    for params in paramList:
        scene = params[0]
        data = 'data/' + scene
        final_budget = params[1]
        output = "output/" + scene + "-" + str(i)
        sh_lr = params[2]

        one_cmd = f'python train-fast.py -s {data} -m {output} --final_budget {final_budget} --shfeature_lr {sh_lr} --iteration 15000'
        two_cmd = f'python render.py -m {output} --skip_train'
        three_cmd = f'python metrics.py -m {output}'
        four_cmd = f'python fps.py -m {output}'

        os.system(one_cmd)
        os.system(two_cmd)
        os.system(three_cmd)
        os.system(four_cmd)

