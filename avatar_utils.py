import subprocess
import os

def generate_avatar_video(audio_path):
    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)
    
    # Run SadTalker inference
    cmd = f"""
    python SadTalker/inference.py \
        --driven_audio {audio_path} \
        --source_image avatar.png \
        --result_dir {output_dir} \
        --still \
        --preprocess full \
        --enhancer gfpgan
    """
    
    subprocess.run(cmd, shell=True)
    
    # Find the latest generated video
    latest_video = sorted([f for f in os.listdir(output_dir) if f.endswith(".mp4")])[-1]
    return os.path.join(output_dir, latest_video)
