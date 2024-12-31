'''

export OUTPUT_DIR="/home/suyixuan/AI/Pose_Estimation/SAM-6D/Data/Example/outputs"

export CAD_PATH=/home/suyixuan/AI/Pose_Estimation/SAM-6D/Data/Example/obj_000005.ply    # path to a given cad model(mm)
export RGB_PATH=/home/suyixuan/AI/Pose_Estimation/SAM-6D/Data/Example/rgb.png           # path to a given RGB image
export DEPTH_PATH=/home/suyixuan/AI/Pose_Estimation/SAM-6D/Data/Example/depth.png       # path to a given depth map(mm)
export CAMERA_PATH=/home/suyixuan/AI/Pose_Estimation/SAM-6D/Data/Example/camera.json    # path to given camera intrinsics
export OUTPUT_DIR=/home/suyixuan/AI/Pose_Estimation/SAM-6D/Data/Example/outputs         # path to a pre-defined file for saving results

export CAD_PATH=/home/suyixuan/AI/Pose_Estimation/SAM-6D/Data/Example/obj_000005.ply
export RGB_PATH=/home/suyixuan/AI/Pose_Estimation/SAM-6D/Data/Example/rgb.png
export DEPTH_PATH=/home/suyixuan/AI/Pose_Estimation/SAM-6D/Data/Example/depth.png
export CAMERA_PATH=/home/suyixuan/AI/Pose_Estimation/SAM-6D/Data/Example/camera.json
export OUTPUT_DIR=/home/suyixuan/AI/Pose_Estimation/SAM-6D/Data/Example/outputs




# 1. 安装 Blender
https://www.blender.org/download/

验证 Blender 是否正常运行： 你可以通过执行以下命令来验证 Blender 是否正常运行：

/home/suyixuan/AI/Pose_Estimation/blender-4.3.2-linux-x64/blender --version

(sam6d) suyixuan@suyixuan-ASUS-TUF-Gaming-F16-FX607JVR-FX607JVR:~/AI/Pose_Estimation/SAM-6D/Render$ /home/suyixuan/AI/Pose_Estimation/blender-4.3.2-linux-x64/blender --version
Blender 4.3.2
	build date: 2024-12-17
	build time: 01:31:14
	build commit date: 2024-12-16
	build commit time: 21:10
	build hash: 32f5fdce0a0a
	build branch: blender-v4.3-release
	build platform: Linux
	build type: Release
	build c flags:  -Wall -Werror=implicit-function-declaration -Wstrict-prototypes -Werror=return-type -Werror=vla -Wmissing-prototypes -Wno-char-subscripts -Wno-unknown-pragmas -Wpointer-arith -Wunused-parameter -Wwrite-strings -Wlogical-op -Wundef -Winit-self -Wmissing-include-dirs -Wno-div-by-zero -Wtype-limits -Wformat-signedness -Wrestrict -Wno-stringop-overread -Wno-stringop-overflow -Wnonnull -Wabsolute-value -Wuninitialized -Wredundant-decls -Wshadow -Wimplicit-fallthrough=5 -Wno-error=unused-but-set-variable  -march=x86-64-v2 -std=gnu11 -pipe -fPIC -funsigned-char -fno-strict-aliasing -ffp-contract=off
	build c++ flags:  -Wuninitialized -Wredundant-decls -Wall -Wno-invalid-offsetof -Wno-sign-compare -Wlogical-op -Winit-self -Wmissing-include-dirs -Wno-div-by-zero -Wtype-limits -Werror=return-type -Wno-char-subscripts -Wno-unknown-pragmas -Wpointer-arith -Wunused-parameter -Wwrite-strings -Wundef -Wcomma-subscript -Wformat-signedness -Wrestrict -Wno-suggest-override -Wuninitialized -Wno-stringop-overread -Wno-stringop-overflow -Wimplicit-fallthrough=5 -Wundef -Wmissing-declarations  -march=x86-64-v2 -pipe -fPIC -funsigned-char -fno-strict-aliasing -ffp-contract=off
	build link flags:  -Wl,--version-script='/home/blender/git/blender-v430/blender.git/source/creator/symbols_unix.map'
	build system: CMake


如果 Blender 正常安装，应该会显示 Blender 版本信息。


export BLENDER_PATH=/home/suyixuan/AI/Pose_Estimation/blender-4.3.2-linux-x64/blender
blenderproc run render_custom_templates.py --output_dir $OUTPUT_DIR --cad_path $CAD_PATH


升级版本的问题 是 Blender 的版本和 BlenderProc 的版本不兼容。
BlenderProc 是一个用于生成 3D 渲染数据的 Python 库，
它需要与 Blender 的版本相匹配才能正常工作。


pip install --upgrade blenderproc





'''