# MoviePy Editing

This project aims to edit a sequence of input videos.
The parameters can be adjusted in code.
**Abilities:**
- Add a Watermark
- Generate 5 random Thumbnails
- Zoom
- Crop
- Resize

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and using.

### Prerequisites

```
pip install -r requirements.txt
```

### Altering the Parameters

To change the specifics, edit `video_param` dictionary in file index.py

```
video_param = {
    'logo_width' : 60,      # Width of Watermark Logo
    'logo_height' : 60,     # Height of Watermark Logo
    'logo_margin_x' : 20,   # Right Margin of Watermark Logo
    'logo_margin_y' : 20,   # Bottom Margin of Watermark Logo

    'crop_margin_x' : 10,   # Horizontal Crop Margin
    'crop_margin_y' : 10,   # Vertical Crop Margin

    'out_height' : 720      # Height of output video
}

All integers assigned above are treated as pixels
```

### Using

- Add all input videos in input folder (Names will be used as folder names in output)
- Add logo.png to current directory (This is used for watermark)
- Run index.py

```
python index.py
```


## Built With

* [MoviePy](https://zulko.github.io/moviepy/) - Python module for video editing

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
