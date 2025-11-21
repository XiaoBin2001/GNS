# Gradient-Driven Natural Selection for Compact 3D Gaussian Splatting

### Xiaobin Deng, Qiuli Yu, Changyu Diao, Min Li, Duanqing Xu

### Zhejiang University

## [Paper]| [arXiv]| [Project Page](https://xiaobin2001.github.io/GNS-web/)|

![figure_intro](assets/figure_intro.png)

3DGS employs a large number of Gaussian primitives to fit scenes, resulting in substantial storage and computational overhead. Existing pruning methods rely on manually designed criteria or introduce additional learnable parameters, yielding suboptimal results. To address this, we propose an natural selection inspired pruning framework that models survival pressure as a regularization gradient field applied to opacity, allowing the optimization gradients—driven by the goal of maximizing rendering quality—to autonomously determine which Gaussians to retain or prune. This process is fully learnable and requires no human intervention. We further introduce an opacity decay technique with a finite opacity prior, which accelerates the selection process without compromising pruning effectiveness. Compared to 3DGS, our method achieves over 0.6 dB PSNR gain under 15% budgets, establishing state-of-the-art performance for compact 3DGS.

<video src="assets/video_psnr_num.mp4"></video>



## Qualitative Result

<video src="assets/bicycle.mp4"></video>

![point](assets/point.png)

## Quantitative Result

![quantitative](assets/quantitative.png)

![figure_score_budget](assets/figure_score_budget.png)

## Environment

Before installing our project, you need to ensure that your local environment for compiling the 3DGS CUDA kernel is properly set up, such as having CUDA Toolkit and Visual Studio installed. We recommend that you first install and run the [original 3DGS repository](https://github.com/graphdeco-inria/gaussian-splatting), and then proceed to install our project upon successful setup.

## Installation

Clone the repository

```
https://github.com/XiaoBin2001/GNS.git
```

Extract the compressed package of submodules-speedy.

Then, you can install the dependencies listed in `environment.yml` following the installation instructions of 3DGS. 

If you are already familiar with installing various 3DGS-based improvements, you may choose to manually install the required libraries. However, please note the following:  

- Ensure that your `pip` version is not too high, otherwise the CUDA kernels in the submodules may fail to install properly.  
- The `numpy` version should be 1.x.x. Sometimes, the default installation may result in `numpy` ≥ 2.0, which you will need to manually downgrade.

## Running

The `budget.txt` file provides the budget parameters we used across various scenes. The "small" version uses 40% of the normal budget, allowing our method to be successfully reproduced even on consumer-grade GPUs such as the RTX 3060. Notably, the performance of the small version still surpasses that of the original 3DGS.

`test.py` provides a simple script to run evaluations in batch mode.

To use this script, you need to create a `data` folder and organize the required 13 scenes in the following structure:

```
data
├── bicycle
│   ├── images
│   └── sparse
├── flowers
├── ...
```

You can also run the code in the same way as 3DGS.

## Parameters

The code has integrated an automatic adjustment mechanism for the regularization learning rate, so you only need to provide the `final-budget` parameter to automatically train a high-quality compact model.

## Scene Visualization

Our work does not introduce additional parameters to the Gaussian ellipsoids, which means you can use any 3DGS viewer to visualize the trained scenes. We recommend [SuperSplat](https://superspl.at/editor) as a viewer.

## Citation

Bibtex
```

```

## Acknowledgments

This project is built upon the open-source code of [TamingGS](https://github.com/humansensinglab/taming-3dgs). We sincerely thank the authors for their excellent work.
