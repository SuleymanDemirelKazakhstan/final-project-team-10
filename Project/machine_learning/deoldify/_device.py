import os
from enum import Enum
from enum import IntEnum

class DeviceId(IntEnum):
    GPU0 = 0,
    GPU1 = 1,
    GPU2 = 2,
    GPU3 = 3,
    GPU4 = 4,
    GPU5 = 5,
    GPU6 = 6,
    GPU7 = 7,
    CPU = 99


class DeviceException(Exception):
    pass

class _Device:
    def __init__(self):
        self.set(DeviceId.CPU)

    def is_gpu(self):
        ''' Returns `True` if the current device is GPU, `False` otherwise. '''
        return self.current() is not DeviceID.CPU
  
    def current(self):
        return self._current_device

    def set(self, device:DeviceId):     
        if device == DeviceId.CPU:
            os.environ['CUDA_VISIBLE_DEVICES']=''
        else:
            os.environ['CUDA_VISIBLE_DEVICES']=str(device.value)
            import torch
            torch.backends.cudnn.benchmark=False
        
        os.environ['OMP_NUM_THREADS']='1'
        self._current_device = device    
        return device