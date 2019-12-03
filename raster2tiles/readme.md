# raster2tiles.py

This script splits a tif into smaller images.

## Input
A tif file
Output directory
Input image resolution
Output image width (Optional - needed if config file not provided)
Output image height (Optional - needed if config file not provided)
Config file (Optional - needed if output width and height not provided as arguments)
Log level - info, warning, error, debug

## Output
Smaller images into separate directories based on output resolution

## Example:

### Config file

```
python raster2tiles.py /Input/Image/Directory/Sentinel.tif /Output/Directory/ --input_resolution=10 --config=config.json -log debug
```

where `config.json`

```
{
    "output_resolution": [
        {"width": 250, "height": 250},
        {"width": 500, "height": 500},
        {"width": 500, "height": 1000},
        {"width": 1000, "height": 500}
    ]
}
```

### With arguments

```
python raster2tiles.py /Input/Image/Directory/Sentinel.tif /Output/Directory/ --input_resolution=10 --output_img_width=500 --output_img_height=500 -log debug
```

## Dependency

`gdal` package is needed

### Install `gdal`

```
pip install gdal
```

Refer to https://pypi.org/project/GDAL/