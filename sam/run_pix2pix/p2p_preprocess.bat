python ../../pix2pix/tools/process.py --input_dir C:/Users/Sa/Desktop/weather/p2p/A --b_dir C:/Users/Sa/Desktop/weather/p2p/B --operation combine --output_dir C:/Users/Sa/Desktop/weather/p2p/combined
echo "done step1"
python ../../pix2pix/tools/split.py --dir C:/Users/Sa/Desktop/weather/p2p/combined
echo "done!"
