
source venv/bin/activate

python zeta_plane.py \
  --xmin -0.1 --xmax 1.1 \
  --ymin -120 --ymax 120 \
  --nx 800 --ny 1500 \
  --output symmetric_strip.png
