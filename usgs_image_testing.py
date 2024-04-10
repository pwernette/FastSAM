from fastsam import FastSAM, FastSAMPrompt
import glob

model = FastSAM('./weights/FastSAM-x.pt')
IMAGE_DIR = './images'
IMAGE_PATH = './images/dogs.jpg'
IMAGE_SIZE = 1024
DEVICE = 'cpu'
everything_results = model(IMAGE_PATH, device=DEVICE, retina_masks=True, conf=0.4, iou=0.9,)
prompt_process = FastSAMPrompt(IMAGE_PATH, everything_results, device=DEVICE)

# everything prompt
ann = prompt_process.everything_prompt()

# # bbox default shape [0,0,0,0] -> [x1,y1,x2,y2]
# ann = prompt_process.box_prompt(bboxes=[[200, 200, 300, 300]])

# # text prompt
# ann = prompt_process.text_prompt(text='a photo of a dog')

# # point prompt
# # points default [[0,0]] [[x1,y1],[x2,y2]]
# # point_label default [0] [1,0] 0:background, 1:foreground
# ann = prompt_process.point_prompt(points=[[620, 360]], pointlabel=[1])

prompt_process.plot(annotations=ann,output_path='./output/dog.jpg',)