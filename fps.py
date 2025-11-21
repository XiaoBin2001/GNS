import torch
from scene import Scene
import os
from tqdm import tqdm
from os import makedirs
from gaussian_renderer import render
from utils.general_utils import safe_state
from argparse import ArgumentParser
from arguments import ModelParams, PipelineParams, get_combined_args
from gaussian_renderer import GaussianModel

import time

def render_set(model_path, name, iteration, views, gaussians, pipeline, background):
    total_fps = 0
    for i in range(10):
        render_path = os.path.join(model_path, name, "ours_{}".format(iteration), "renders")
        gts_path = os.path.join(model_path, name, "ours_{}".format(iteration), "gt")

        makedirs(render_path, exist_ok=True)
        makedirs(gts_path, exist_ok=True)

        total_time = 0
        for idx, view in enumerate(tqdm(views, desc="Rendering progress")):
            start_time = time.time()  # 开始计时
            rendering = render(view, gaussians, pipeline, background)["render"]
            if i > 4:
                total_time += time.time() - start_time  # 记录该次渲染的用时
        if i > 4:
            total_fps = total_fps + 1 / (total_time / len(views))
    num = int(gaussians.get_opacity.shape[0])
    return int(total_fps) / 5, num

def render_sets(dataset : ModelParams, iteration : int, pipeline : PipelineParams):
    with torch.no_grad():
        gaussians = GaussianModel(dataset.sh_degree)
        scene = Scene(dataset, gaussians, load_iteration=iteration, shuffle=False)

        bg_color = [1,1,1] if dataset.white_background else [0, 0, 0]
        background = torch.tensor(bg_color, dtype=torch.float32, device="cuda")

        return render_set(dataset.model_path, "test", scene.loaded_iter, scene.getTestCameras(), gaussians, pipeline, background)

if __name__ == "__main__":
    # Set up command line argument parser
    parser = ArgumentParser(description="Testing script parameters")
    model = ModelParams(parser, sentinel=True)
    pipeline = PipelineParams(parser)
    parser.add_argument("--iteration", default=-1, type=int)
    parser.add_argument("--skip_train", action="store_true")
    parser.add_argument("--skip_test", action="store_true")
    parser.add_argument("--quiet", action="store_true")
    args = get_combined_args(parser)
    print("Rendering " + args.model_path)

    # Initialize system state (RNG)
    safe_state(args.quiet)
    fps, num = render_sets(model.extract(args), args.iteration, pipeline.extract(args))

    file_path = os.path.join(args.model_path, 'fps.txt')
    print(fps)
    # 将浮点数保存到文件
    with open(file_path, 'w') as f:
        f.write(f"{fps}\n")
        f.write(f"{num}\n")



