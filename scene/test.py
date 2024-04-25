import numpy as np
def read_extrinsics_text_for_dust3r(path):
    images = {}
    with open(path) as f:
        lines = f.readlines()
        assert len(lines) != 0, "No extrinsics found in file!"
        assert len(lines) % 5 == 0, "Extrinsics file not formatted correctly!"
        for i in range(0, len(lines), 5):
            image_name = lines[i].split(" ")[0]
            extr = np.zeros((4, 4))
            for j in range(4):
                lines[i+1+j] = lines[i+1+j].split(" ")
                extr[j, 0] = float(lines[i+1+j][0])
                extr[j, 1] = float(lines[i+1+j][1])
                extr[j, 2] = float(lines[i+1+j][2])
                extr[j, 3] = float(lines[i+1+j][3])
            images[image_name] = extr
    return images

def read_intrinsics_text_for_dust3r(path):
    images = {}
    with open(path) as f:
        lines = f.readlines()
        assert len(lines) != 0, "No intrinsics found in file!"
        assert len(lines) % 4 == 0, "Intrinsics file not formatted correctly!"
        for i in range(0, len(lines), 4):
            image_name = lines[i].split(" ")[0]
            intr = np.zeros((3, 3))
            for j in range(3):
                lines[i+1+j] = lines[i+1+j].split(" ")
                intr[j, 0] = float(lines[i+1+j][0])
                intr[j, 1] = float(lines[i+1+j][1])
                intr[j, 2] = float(lines[i+1+j][2])
            images[image_name] = intr
    return images


# print("extrinsics: ", read_extrinsics_text_for_dust3r("../dataset/360_v2/bicycle/test5/dust3r/extrinsics.txt"))
# print("intrinsics: ", read_intrinsics_text_for_dust3r("../dataset/360_v2/bicycle/test5/dust3r/intrinsics.txt"))