from fastai.core import *
from fastai.vision import *
from .filters import IFilter, MasterFilter, ColorizerFilter
from .generators import gen_inference_wide
from tensorboardX import SummaryWriter
from PIL import Image
import gc
import cv2




class ModelImageVisualizer:
    def __init__(self, filter: IFilter):
        self.filter = filter

    def _clean_mem(self):
        torch.cuda.empty_cache()
        # gc.collect()
    
    def get_transformed_image(
        self, img: Image, render_factor: int = None, post_process: bool = True,
    ) -> Image:
        self._clean_mem()
        filtered_image = self.filter.filter(
            img, img, render_factor=render_factor,post_process=post_process
        )

        return filtered_image


def get_image_colorizer(
    root_folder: Path = Path('./'),
    weights_name: str = 'ColorizeStable_gen',
    results_dir='result_images',
    render_factor: int = 35
) -> ModelImageVisualizer:
    learn = gen_inference_wide(root_folder=root_folder, weights_name=weights_name)
    filtr = MasterFilter([ColorizerFilter(learn=learn)], render_factor=render_factor)
    vis = ModelImageVisualizer(filtr)
    return vis