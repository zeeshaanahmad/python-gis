import argparse
from datetime import datetime
import gdal
import json
import logging
import os
import sys

parser = argparse.ArgumentParser(description='Split a large tiff file into smaller images.')

parser.add_argument('input_file', type=str,
                    help='Path of input tif file')
parser.add_argument('output_dir', type=str,
                    help='Output directory to store the images. Creates new directory if not available.')
parser.add_argument('--input_resolution', dest='input_resolution', type=int, nargs='?', required=True,
                    help='Resolution of input image without unit. e.g. if 10m, enter only 10. If 1km enter 1000')
parser.add_argument('--output_img_width', dest='output_img_width', type=int, nargs='?',
                    help='Width in pixels of output images without e.g. 50 for 50px')
parser.add_argument('--output_img_height', dest='output_img_height', type=int, nargs='?',
                    help='Height in pixels of output images without e.g. 50 for 50px')
parser.add_argument('--config', dest='config', type=str, nargs='?',
                    help='Path to config.json file')
parser.add_argument("-log", "--log", help="Provide logging level. Example --log debug", choices=['debug', 'info', 'warning'], default='info')

args = parser.parse_args()

level_config = {'debug': logging.DEBUG, 'info': logging.INFO, 'warning': logging.WARNING, 'error': logging.ERROR}
log_level = args.log
log_level = level_config[log_level.lower()]
logging.basicConfig(level=log_level, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logger = logging.getLogger(__name__) 

logger.debug(args)

output_resolutions = []

if args.config and os.path.isfile(args.config):
    logger.debug("configuration file: {} provided and exists".format(args.config))
    with open(args.config) as json_file:
        logger.info("reading config file: {0}".format(args.config))
        config = json.load(json_file)
        logger.debug("loaded config file: {0}".format(args.config))
        logger.debug("reading output resolutions from config file: {}".format(args.config))
        output_resolutions = config['output_resolution']
        logger.info("output resolutions: {0}".format(output_resolutions))
elif args.output_img_height and args.output_img_height > 0 and args.output_img_width and args.output_img_width > 0:
    logger.debug("output resolution provided via arguments, width: {0}, height: {1} ".format(args.output_img_width, args.output_img_height))
    output_resolutions = [{"width": args.output_img_width, "height": args.output_img_height}]
    logger.info("output resolutions: {0}".format(output_resolutions))
else:
    logger.error("neither config file nor arguments provided for output resolution")
    sys.exit()

if not os.path.isdir(args.output_dir):
    logger.debug("directory: {0} does not exist".format(args.output_dir))
    os.mkdir(args.output_dir)
    logger.info("directory: {0} created".format(args.output_dir))

if not args.input_file.lower().endswith(('.tif', '.jp2')):
    logger.error("Invalid input file: {0}".format(args.input_file))
    sys.exit()

logger.info("reading input raster: {0}".format(args.input_file))
ds = gdal.Open(args.input_file)
xsize = ds.RasterXSize
logger.info("raster x size: {0}".format(xsize))
ysize = ds.RasterYSize
logger.info("raster y size: {0}".format(ysize))

# band = ds.GetRasterBand(3)
# xsize = band.XSize
# ysize = band.YSize

for res in output_resolutions:
    logger.debug("working on resolution: {0}".format(res))
    tile_size_x = res["width"]
    tile_size_y = res["height"]
    logger.info("output width: {0}, output height: {1}".format(tile_size_x, tile_size_y))

    time_creation = datetime.now().strftime("%Y%m%d%H%M%S%f")

    out_path = "{0}/{1}_{2}_{3}_{4}/".format(args.output_dir.rstrip('/'), args.output_dir.rstrip('/').split("/")[-1], tile_size_x, tile_size_y, time_creation)
    output_filename = 'tile_'

    logger.info("creating directory: {0}".format(out_path))
    os.mkdir(out_path)
    logger.debug("directory: {0} created".format(out_path))

    for i in range(0, xsize, tile_size_x):
        for j in range(0, ysize, tile_size_y):
            logger.info("window of xoffset: {0}, yoffset: {1} of size xsize: {2}, ysize: {3}".format(i, j, tile_size_y, tile_size_y))
            com_string = "gdal_translate -of GTIFF -srcwin " + str(i)+ ", " + str(j) + ", " + str(tile_size_x) + ", " + str(tile_size_y) + " " + str(args.input_file) + " " + str(out_path) + str(output_filename) + str(i) + "_" + str(j) + ".tif"
            logger.debug("Executing ->  {0}".format(com_string))
            os.system(com_string)