import os
import ipdb

path = "E:\\电影\\uc\\gen_m3u8"

with open(os.path.join(path, "result_cmd.txt"), "w") as f:
    for i in os.listdir(path):
        cmd_str = "ffmpeg -allowed_extensions ALL -i "+i+" -c copy "+i.split(".")[0]+".mp4"
        f.write(cmd_str+"\n")
