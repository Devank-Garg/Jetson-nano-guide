

# Jetson Nano Complete Guide

This comprehensive guide will walk you through setting up and utilizing the Jetson Nano Developer Kit for AI applications. Whether you're interested in running pre-trained models or developing and deploying your custom models, this guide has you covered.

## 1. Download the Jetson Nano Developer Kit SD Card Image

- Begin by downloading the Jetson Nano Developer Kit SD Card Image from the official source.

## 2. Write the Image to Your microSD Card

- Use Etcher or a similar tool to write the Jetson Nano Developer Kit SD Card Image to your microSD card. This will serve as the bootable system for your Jetson Nano.

## 3. Setup Ubuntu on First-Time Launch

- After writing the image to the microSD card, insert it into the Jetson Nano and power it on. Follow the on-screen instructions to set up Ubuntu on the first-time launch.

## 4. Get Started with Hello AI World

- To get familiar with the basics and the general workflow on Jetson Nano, visit the "Hello AI World" GitHub repository. It provides valuable insights into how things work on Jetson Nano.

## 5. Choose Your Deployment Option

- You have two deployment options:
    - **Run from Docker:** Start using Docker containers without the need for extensive setup.
    - **Build from Source:** Build the project from source code and then run inference. Follow the provided links for detailed instructions on each approach.

## 6. Post-Build Instructions

- If you have built the project from source, follow these additional instructions:

## 7. Clone the Jetson-Inference Library

- Clone the "jetson-inference" library for further capabilities.

   ```shell
   $ cd jetson-inference/build/aarch64/bin
   ```

- Use the following command to move into this directory.

   ```shell
   $ ./imagenet.py images/orange_0.jpg images/test/output_0.jpg
   ```

- Run the classification on an image (e.g., `orange_0.jpg`) and save the output as `output_0.jpg`. You can process multiple images in a single run using wildcard notation (e.g., `imagename_*.jpg` as input and `imagename_%i.jpg` as output).

## 8. Explore Available Models

- Check out all the pre-trained models and run them directly from the terminal.

## 9. Test Models on Live Stream

- Copy the script from the provided folder and run it to test the models on a live stream and save the video output.

    ```shell
    $ cd jetson-inference/tools
    $ ./download-models.sh
    ```

- Use the above commands to download various available models.

## Running Your Custom Model on Jetson Nano

If you want to run your custom model on Jetson Nano, follow these steps:

1. Train your model and save it as `model.pt` or directly as a weights file if possible (save it as a PyTorch model).

2. Convert the model to a `model.wts` file if it's not already in that format.

3. Build the TensorRT engine for the generated `model.wts` file.

4. Run the `app.py` script, which will utilize the custom model for inference. All necessary files for this process will be available in the provided repository link.

For convenience, we've included modified code in the repository for running inference and saving video output for all models. The following scripts are available:

- `My-detection.py`: Use this script to directly run pretrained models and save the results. Simply change the model according to your requirements.

- `App2.py`: This script is designed for running your custom YOLO model and saving the results. Refer to the above steps for all dependent files.

Now you're all set to harness the power of the Jetson Nano Developer Kit for your AI projects. Enjoy exploring its capabilities and deploying custom models as needed.
