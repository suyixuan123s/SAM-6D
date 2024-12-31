'''

 pip install numpy==1.23.0


(sam6d) suyixuan@suyixuan-ASUS-TUF-Gaming-F16-FX607JVR-FX607JVR:~/AI/Pose_Estimation/SAM-6D/Instance_Segmentation_Model$ python run_inference_custom.py --segmentor_model $SEGMENTOR_MODEL --output_dir $OUTPUT_DIR --cad_path $CAD_PATH --rgb_path $RGB_PATH --depth_path $DEPTH_PATH --cam_path $CAMERA_PATH

A module that was compiled using NumPy 1.x cannot be run in
NumPy 2.0.2 as it may crash. To support both 1.x and 2.x
versions of NumPy, modules must be compiled with NumPy 2.0.
Some module may need to rebuild instead e.g. with 'pybind11>=2.12'.

If you are a user of the module, the easiest solution will be to
downgrade to 'numpy<2' or try to upgrade the affected module.
We expect that some modules will need time to support NumPy 2.

Traceback (most recent call last):  File "/home/suyixuan/AI/Pose_Estimation/SAM-6D/Instance_Segmentation_Model/run_inference_custom.py", line 21, in <module>
    from torchvision.utils import save_image
  File "/home/suyixuan/anaconda3/envs/sam6d/lib/python3.9/site-packages/torchvision/__init__.py", line 6, in <module>
    from torchvision import datasets, io, models, ops, transforms, utils
  File "/home/suyixuan/anaconda3/envs/sam6d/lib/python3.9/site-packages/torchvision/models/__init__.py", line 17, in <module>
    from . import detection, optical_flow, quantization, segmentation, video
  File "/home/suyixuan/anaconda3/envs/sam6d/lib/python3.9/site-packages/torchvision/models/detection/__init__.py", line 1, in <module>
    from .faster_rcnn import *
  File "/home/suyixuan/anaconda3/envs/sam6d/lib/python3.9/site-packages/torchvision/models/detection/faster_rcnn.py", line 16, in <module>
    from .anchor_utils import AnchorGenerator
  File "/home/suyixuan/anaconda3/envs/sam6d/lib/python3.9/site-packages/torchvision/models/detection/anchor_utils.py", line 10, in <module>
    class AnchorGenerator(nn.Module):
  File "/home/suyixuan/anaconda3/envs/sam6d/lib/python3.9/site-packages/torchvision/models/detection/anchor_utils.py", line 63, in AnchorGenerator
    device: torch.device = torch.device("cpu"),
/home/suyixuan/anaconda3/envs/sam6d/lib/python3.9/site-packages/torchvision/models/detection/anchor_utils.py:63: UserWarning: Failed to initialize NumPy: _ARRAY_API not found (Triggered internally at ../torch/csrc/utils/tensor_numpy.cpp:84.)
  device: torch.device = torch.device("cpu"),
/home/suyixuan/anaconda3/envs/sam6d/lib/python3.9/site-packages/hydra/_internal/defaults_list.py:251: UserWarning: In 'ISM_sam.yaml': Defaults list is missing `_self_`. See https://hydra.cc/docs/1.2/upgrades/1.0_to_1.1/default_composition_order for more information
  warnings.warn(msg, UserWarning)
INFO:root:Initializing model
INFO:root:Loading SAM model from ./checkpoints/segment-anything/
INFO:root:Init CustomSamAutomaticMaskGenerator done!
INFO:torch.distributed.nn.jit.instantiator:Created a temporary directory at /tmp/tmpyj93cf0n
INFO:torch.distributed.nn.jit.instantiator:Writing /tmp/tmpyj93cf0n/_remote_module_non_scriptable.py
INFO:dinov2:using MLP layer as FFN
INFO:root:Init CustomDINOv2 done!
INFO:root:Init CustomDINOv2 with full size=640 and proposal size=224 done!
INFO:root:Init CNOS done!
INFO:root:Moving models to cuda done!
INFO:root:Initializing template
Traceback (most recent call last):
  File "/home/suyixuan/AI/Pose_Estimation/SAM-6D/Instance_Segmentation_Model/run_inference_custom.py", line 224, in <module>
    run_inference(
  File "/home/suyixuan/AI/Pose_Estimation/SAM-6D/Instance_Segmentation_Model/run_inference_custom.py", line 134, in run_inference
    image = torch.from_numpy(np.array(image.convert("RGB")) / 255).float()
RuntimeError: Numpy is not available
(sam6d) suyixuan@suyixuan-ASUS-TUF-Gaming-F16-FX607JVR-FX607JVR:~/AI/Pose_Estimation/SAM-6D/Instance_Segmentation_Model$ conda list numpy
# packages in environment at /home/suyixuan/anaconda3/envs/sam6d:
#
# Name                    Version                   Build  Channel
numpy                     2.0.2                    pypi_0    pypi
(sam6d) suyixuan@suyixuan-ASUS-TUF-Gaming-F16-FX607JVR-FX607JVR:~/AI/Pose_Estimation/SAM-6D/Instance_Segmentation_Model$ pip install numpy==1.21.6
Collecting numpy==1.21.6
  Downloading numpy-1.21.6-cp39-cp39-manylinux_2_12_x86_64.manylinux2010_x86_64.whl.metadata (2.1 kB)
Downloading numpy-1.21.6-cp39-cp39-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (15.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 15.7/15.7 MB 31.1 MB/s eta 0:00:00
Installing collected packages: numpy
  Attempting uninstall: numpy
    Found existing installation: numpy 2.0.2
    Uninstalling numpy-2.0.2:
      Successfully uninstalled numpy-2.0.2
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
contourpy 1.3.0 requires numpy>=1.23, but you have numpy 1.21.6 which is incompatible.
matplotlib 3.9.4 requires numpy>=1.23, but you have numpy 1.21.6 which is incompatible.
pandas 2.2.3 requires numpy>=1.22.4; python_version < "3.11", but you have numpy 1.21.6 which is incompatible.
scikit-image 0.24.0 requires numpy>=1.23, but you have numpy 1.21.6 which is incompatible.
scipy 1.13.1 requires numpy<2.3,>=1.22.4, but you have numpy 1.21.6 which is incompatible.
Successfully installed numpy-1.21.6
(sam6d) suyixuan@suyixuan-ASUS-TUF-Gaming-F16-FX607JVR-FX607JVR:~/AI/Pose_Estimation/SAM-6D/Instance_Segmentation_Model$ pip install numpy==1.22.4
Collecting numpy==1.22.4
  Downloading numpy-1.22.4-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (2.0 kB)
Downloading numpy-1.22.4-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (16.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.8/16.8 MB 40.5 MB/s eta 0:00:00
Installing collected packages: numpy
  Attempting uninstall: numpy
    Found existing installation: numpy 1.21.6
    Uninstalling numpy-1.21.6:
      Successfully uninstalled numpy-1.21.6
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
contourpy 1.3.0 requires numpy>=1.23, but you have numpy 1.22.4 which is incompatible.
matplotlib 3.9.4 requires numpy>=1.23, but you have numpy 1.22.4 which is incompatible.
scikit-image 0.24.0 requires numpy>=1.23, but you have numpy 1.22.4 which is incompatible.
Successfully installed numpy-1.22.4
(sam6d) suyixuan@suyixuan-ASUS-TUF-Gaming-F16-FX607JVR-FX607JVR:~/AI/Pose_Estimation/SAM-6D/Instance_Segmentation_Model$ pip install numpy==1.23.0
Collecting numpy==1.23.0
  Downloading numpy-1.23.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (2.2 kB)
Downloading numpy-1.23.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (17.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 17.1/17.1 MB 46.8 MB/s eta 0:00:00
Installing collected packages: numpy
  Attempting uninstall: numpy
    Found existing installation: numpy 1.22.4
    Uninstalling numpy-1.22.4:
      Successfully uninstalled numpy-1.22.4
Successfully installed numpy-1.23.0
(sam6d) suyixuan@suyixuan-ASUS-TUF-Gaming-F16-FX607JVR-FX607JVR:~/AI/Pose_Estimation/SAM-6D/Instance_Segmentation_Model$ python run_inference_custom.py --segmentor_model $SEGMENTOR_MODEL --output_dir $OUTPUT_DIR --cad_path $CAD_PATH --rgb_path $RGB_PATH --depth_path $DEPTH_PATH --cam_path $CAMERA_PATH
/home/suyixuan/anaconda3/envs/sam6d/lib/python3.9/site-packages/hydra/_internal/defaults_list.py:251: UserWarning: In 'ISM_sam.yaml': Defaults list is missing `_self_`. See https://hydra.cc/docs/1.2/upgrades/1.0_to_1.1/default_composition_order for more information
  warnings.warn(msg, UserWarning)
INFO:root:Initializing model
INFO:root:Loading SAM model from ./checkpoints/segment-anything/
INFO:root:Init CustomSamAutomaticMaskGenerator done!
INFO:torch.distributed.nn.jit.instantiator:Created a temporary directory at /tmp/tmplatwiff1
INFO:torch.distributed.nn.jit.instantiator:Writing /tmp/tmplatwiff1/_remote_module_non_scriptable.py
INFO:dinov2:using MLP layer as FFN
INFO:root:Init CustomDINOv2 done!
INFO:root:Init CustomDINOv2 with full size=640 and proposal size=224 done!
INFO:root:Init CNOS done!
INFO:root:Moving models to cuda done!
INFO:root:Initializing template
/home/suyixuan/AI/Pose_Estimation/SAM-6D/Instance_Segmentation_Model/run_inference_custom.py:86: DeprecationWarning: Starting with ImageIO v3 the behavior of this function will switch to that of iio.v3.imread. To keep the current behavior (and make this warning disappear) use `import imageio.v2 as imageio` or call `imageio.v2.imread` directly.
  depth = np.array(imageio.imread(depth_path)).astype(np.int32)
(sam6d) suyixuan@suyixuan-ASUS-TUF-Gaming-F16-FX607JVR-FX607JVR:~/AI/Pose_Estimation/SAM-6D/Instance_Segmentation_Model$




'''