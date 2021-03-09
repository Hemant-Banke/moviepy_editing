from moviepy.editor import *
from moviepy.video.fx.crop import crop

from os import listdir, mkdir
from os.path import isfile, isdir, join
import shutil
from PIL import Image
import random

count = 0
video_param = {
    'logo_width' : 60,
    'logo_height' : 60,
    'logo_margin_x' : 20,
    'logo_margin_y' : 20,
    'crop_margin_x' : 10,
    'crop_margin_y' : 10,
    'out_height' : 720
}


def manip_video(vid_name):
    global count
    (vid_title, vid_ext) = vid_name.split('.')[:2]

    # if (vid_ext != 'mp4'):
    #     print('Not an mp4 video :(')
    #     return

    count += 1

    # Open Video
    stream = VideoFileClip('input/' + vid_name)

    # Manipulate Video

    # 1. Zoom
    stream = crop(
        stream,
        x1 = video_param['crop_margin_x'],
        y1 = video_param['crop_margin_y'],
        x2 = stream.size[0] - video_param['crop_margin_x'],
        y2 = stream.size[1] - video_param['crop_margin_y']).resize(height = video_param['out_height'])


    # 2. Watermark
    logo = (ImageClip("logo.png")
            .set_duration(stream.duration)
            .resize(height = video_param['logo_height'], width = video_param['logo_width'])
            .margin(right = video_param['logo_margin_x'], bottom = video_param['logo_margin_y'], opacity = 0)
            .set_pos(("right","bottom")))

    stream = CompositeVideoClip([stream, logo])

    # Write Output
    out_name = "{0}-{1}".format(count, vid_title)
    if (isdir('output/'+out_name)):
        shutil.rmtree('output/'+out_name)
    mkdir('output/'+out_name)

    out_path = 'output/{0}/output.{1}'.format(out_name, vid_ext)
    stream.write_videofile(out_path, audio = True)

    # Create Thumnails
    print('Generating Thumbnails')
    duration = int(stream.duration)
    thumb_frames = random.sample(range(1, duration), 5)
    for thumb_frame in thumb_frames:
        frame = stream.get_frame(thumb_frame)
        thumb = Image.fromarray(frame)
        thumb.save('output/{0}/{1}.jpg'.format(out_name, thumb_frame))



# Check Logo
if (isfile('logo.png')):
    print('Found Logo')
else:
    print('Logo not found!')
    exit()


# Check Output
if (isdir('output')):
    print('Found Output folder')
else:
    mkdir('output')
    print('Created Output folder')

out_files = listdir('output')
if (len(out_files) > 0):
    is_outclear = ''
    while (is_outclear.upper() != 'Y' and is_outclear.upper() != 'N'):
        is_outclear = input("Do you want to clear the output (Found {0} outputs) (Y/N)? ".format(len(out_files)))

    if (is_outclear.upper() == 'Y'):
        # Delete all directories
        for dirc in listdir('output'):
            dir_path = join('output', dirc)
            try:
                if isdir(dir_path):
                    shutil.rmtree(dir_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (dir_path, e))


# Start Input Batch
files = listdir('input')
print('Starting new batch... ({0} videos found)'.format(len(files)))

for file in files:
    print('---------------------------------------------------------------')
    print('Processing video : ' + file)
    manip_video(file)
    print('---------------------------------------------------------------')