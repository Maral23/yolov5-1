import json 
from datetime import datetime
import torch
import torch.backends.cudnn as cudnn
from utils.general import (LOGGER, check_file, check_img_size, check_imshow, check_requirements, colorstr, cv2,
                           increment_path, non_max_suppression, print_args, scale_coords, strip_optimizer, xyxy2xywh)


#function to create json log
def create_json(det, gn):

    #craeting coordinate and class variables from detection 
    for *xyxy, conf, cls in reversed(det):

        xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / gn).view(-1).tolist()  # normalized xywh
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        date = now.strftime("%x")
        ppe_type = round(cls.item())
        coordinates = str(xywh)
        manager = "Joshua Smith"
        location = 'Factory 1'
        camera = 1

        # appending into text file - in my case no need to save in txt 
        # DO NOT FORGET TO PROVIDE TXT_PATH IN FUNCTION IF NEEDED
        # with open(f'{txt_path}.txt', 'a') as f:
        #         f.write(('%g ' * len(line)).rstrip() % line + '\n')

        # my code to save results in json file 
        with open('log_json.json', 'a') as f:
            dict1 = { "Manager": manager,'Location': location, "PPE": ppe_type, 'Coordinates': coordinates, 'Date': date, 'Time': time, "Camera ID": camera}
            f.write('\n') # to add indent 
            json.dump(dict1, f, indent = 4, sort_keys = False)
            f.write('\n') # to add indent 
            f.close()


    return cls
