# 2D ball collisions

This project was aimed at simulating classical collisions of balls (eg like billard balls) on the plane for `Object programming and Design` classes at univeristy.

To use this project create a python virtual enviroment, once it's activated execute the following command from the main directory:
* `sh install.sh`

Sample results are present in the [demo notebook](https://github.com/wkondrusiewicz/2D_ball_collisions/blob/master/demo/run_simulation.ipynb). After running this notebook execute the following command (firstly you have `cd` to `demo/plots`):
* `ffmpeg -framerate 60 -i img%06d.png output.mp4`
It will produce a movie made of images gathered during the simulation; a sample movie is present [here](https://github.com/wkondrusiewicz/2D_ball_collisions/blob/master/demo/output.mp4)
