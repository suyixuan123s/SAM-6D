'''
1. Preparation
Please clone the repository locally:

git clone https://github.com/JiehongLin/SAM-6D.git
Install the environment and download the model checkpoints:

cd SAM-6D
sh prepare.sh
We also provide a docker image for convenience.

### Create conda environment
conda env create -f environment.yaml
conda activate sam6d

### Install pointnet2
cd Pose_Estimation_Model/model/pointnet2
python setup.py install
cd ../../../

### Download ISM pretrained model
cd Instance_Segmentation_Model
python download_sam.py
python download_fastsam.py
python download_dinov2.py
cd ../

### Download PEM pretrained model
cd Pose_Estimation_Model
python download_sam6d-pem.py



2. Evaluation on the custom data
# set the paths
export CAD_PATH=Data/Example/obj_000005.ply    # path to a given cad model(mm)
export RGB_PATH=Data/Example/rgb.png           # path to a given RGB image
export DEPTH_PATH=Data/Example/depth.png       # path to a given depth map(mm)
export CAMERA_PATH=Data/Example/camera.json    # path to given camera intrinsics
export OUTPUT_DIR=Data/Example/outputs         # path to a pre-defined file for saving results

# run inference
cd SAM-6D
sh demo.sh

# set the paths
export CAD_PATH=/home/suyixuan/AI/Pose_Estimation/SAM-6D/Data/Example/obj_000005.ply
export RGB_PATH=/home/suyixuan/AI/Pose_Estimation/SAM-6D/Data/Example/rgb.png
export DEPTH_PATH=/home/suyixuan/AI/Pose_Estimation/SAM-6D/Data/Example/depth.png
export CAMERA_PATH=/home/suyixuan/AI/Pose_Estimation/SAM-6D/Data/Example/camera.json
export OUTPUT_DIR=/home/suyixuan/AI/Pose_Estimation/SAM-6D/Data/Example/outputs

# run inference
# Render CAD templates
cd Render
blenderproc run render_custom_templates.py --output_dir $OUTPUT_DIR --cad_path $CAD_PATH #--colorize True


# Run instance segmentation model
export SEGMENTOR_MODEL=sam

cd ../Instance_Segmentation_Model
python run_inference_custom.py --segmentor_model $SEGMENTOR_MODEL --output_dir $OUTPUT_DIR --cad_path $CAD_PATH --rgb_path $RGB_PATH --depth_path $DEPTH_PATH --cam_path $CAMERA_PATH


# Run pose estimation model
export SEG_PATH=$OUTPUT_DIR/sam6d_results/detection_ism.json

cd ../Pose_Estimation_Model
python run_inference_custom.py --output_dir $OUTPUT_DIR --cad_path $CAD_PATH --rgb_path $RGB_PATH --depth_path $DEPTH_PATH --cam_path $CAMERA_PATH --seg_path $SEG_PATH




'''
