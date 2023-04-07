# SHGtoSparks_part_2
This is the second of two repositories that contains data and code for the paper “Prediction of fast subcellular Ca2+ signals based on subcellular structures in label-free second harmonic generation microscopy measurements”

Data set:

The raw data set consists of image pairs of second harmonic generation (SHG) and two photon microscopy measurements. They were part of the following publication:

Georgiev, T., Zapiec, B., Forderer, M., Fink, R. H. A. & Vogel, M. Colocalization properties of elementary Ca(2+) release signals with structures specific to the contractile filaments and the tubular system of intact mouse skeletal muscle fibers. J Struct Biol 192, 366-375 (2015). https://doi.org:10.1016/j.jsb.2015.09.018

I provide here a file, img_1_test.tif, with SHG measurements corresponding to Exp_1_SHG.tif (see SHTtoSparks_part_1). This file can be used as input of the image translation algorithm and will output, when the checkpoint is restored, the predicted Ca2+ signals as 256x256 pixel images. These 256x256 pixel images can be stitched to Exp_1_P.tif (512x512 pixel) with another provided algorithm.

I provide 3 example images for the training, test and validation data set.

Two files for the used checkpoint are provided: ckpt-35.data-00000-of-00001 and ckpt-35.index.

Software:

The following software was used in the paper: Python, Jupyter, Spyder, Tensorflow, Tensorflow_io, Keras, Scikit learn, Scikit image, Numpy, Matplotlib, Scipy, Tifffile, Os, Pathlib, Time, Datetime, IPython, Xlsxwriter, ImageJ, Fiji, ChimeraX, https://www.tensorflow.org/tutorials/generative/pix2pix and https://github.com/embl-bio-it/image-analysis-with-python/blob/master/session-3to5/image_analysis_tutorial_solutions.ipynb.
Pearson correlation coefficients were calculated with Scipy, Matthews correlation coefficients were calculated with Scikit learn, structural similarity index (SSIM) and mean squared error (SME) were calculated with Scikit image. The algorithms for the calculation of Pearson correlation coefficients, Matthews correlation coefficients, structural similarity index (SSIM) and mean squared error (SME) will be provided upon request.
The following software version were used in this repository:
Stitch algorithm:

Python (version: 3.7.4), IPython (version: 7.8.0), Spyder (version: 3.3.6), Numpy (version: 1.21.6), Tifffile (version: 2021.11.2)


Image translation algorithm:

Python (version: 3.9.13), Tensorflow (version: 2.8.0), Tensorflow_io (version: 0.25.0), Keras (version: 2.8.0), IPython (version: 8.4.0), Jupyter (version: 6.4.12), Numpy (version: 1.23.1), Tifffile (version: 2022.10.10), Matplotlib (version: 3.6.1), Scipy (version: 1.9.1)


Algorithms:

Image stitch algorithm

Image translation algorithm: The image translation algorithm was taken from https://www.tensorflow.org/tutorials/generative/pix2pix with minor modifications. Cells with modified code are marked in SHGtoSparks.ipynb with change. New comments are marked as new and cell 30 is completely new.

Hardware:

Intel(R) Core(TM) i7-9850H CPU 2.60GHz   2.59 GHz, RAM 64 GB, NVIDIA Quadro RTX 3000 6GB
Running time:

Running time for the small data sets provided here was less than 15 s for each algorithm.
