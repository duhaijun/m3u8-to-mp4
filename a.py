# -- coding: utf-8 --
import os
import ipdb

path = "E:\\电影\\uc\\source_m3u8"

for m3u8_file in os.listdir(path):
    if len(m3u8_file.strip().split(".")) > 1:
        if m3u8_file.strip().split(".")[-1] == "m3u8":
            # mp4 file name
            name = m3u8_file.strip().split(".")[0].strip().replace(",", "").replace(" ", "")
            with open(os.path.join(path, m3u8_file), "r") as f:
                context = f.read()
                just = context.replace("/storage/emulated/0/UCDownloads/VideoData", "E:\\\\电影\\\\uc").replace("//", "\\\\").replace("/", "\\\\")
            with open("E:\\电影\\uc\\gen_m3u8\\"+name[:int(len(name)/2)]+".m3u8", "w") as d:
                d.write(just)
