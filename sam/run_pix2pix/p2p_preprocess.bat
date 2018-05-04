c:\python36\python.exe pix2pix/tools/process.py --input_dir C:/Users/Sa/Desktop/weather/p2p/b2 --b_dir C:/Users/Sa/Desktop/weather/p2p/radar --operation combine --output_dir C:/Users/Sa/Desktop/weather/p2p/combined
echo "done step1"
c:\python36\python.exe pix2pix/tools/split.py --dir C:/Users/Sa/Desktop/weather/p2p/combined
echo "done!"
