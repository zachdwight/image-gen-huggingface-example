# AI Image Generation with 🤗 Diffusers

---

This repository contains a Python script that leverages the Hugging Face `diffusers` library to generate images from a text prompt. It utilizes the `black-forest-labs/FLUX.1-dev` model to create unique visuals, with a focus on managing potential CUDA memory issues.

---
## Features

* **Text-to-Image Generation**: Generate images from a given text prompt using a powerful pre-trained diffusion model.
* **CUDA Memory Management**: Includes a commented-out option to help mitigate CUDA allocation issues.
* **VRAM Optimization**: Employs sequential CPU offloading to handle large models like FLUX.1-dev, making it more accessible on systems with limited VRAM.
* **Batch Image Creation**: Generates a series of images with a unique naming convention.

---
## Requirements

Before running the script, ensure you have the following installed:

* **Python 3.8+**
* **Hugging Face Hub Token**: You'll need a Hugging Face account and an access token to download the `FLUX.1-dev` model. You can obtain one from your [Hugging Face settings page](https://huggingface.co/settings/tokens).
* **Required Python Libraries**: Install them using pip:
    ```bash
    pip install torch diffusers transformers accelerate pillow
    ```

---
## Usage

1.  **Set up your Hugging Face Token**:
    Make sure you have logged in to Hugging Face or have your token configured. You can do this by running `huggingface-cli login` in your terminal and pasting your token, or by setting the `HF_HOME` environment variable.

2.  **Run the script**:
    ```bash
    python your_script_name.py
    ```
    (Replace `your_script_name.py` with the actual name of your Python file.)

The script will generate 7 images based on the specified prompt and save them as `spy_with_bird_1.png` to `spy_with_bird_7.png` in the same directory.

---
## Code Details

* **CUDA Allocation**: The line `os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "max_split_size_mb:2048"` is commented out but can be uncommented if you encounter CUDA out-of-memory errors. This helps in managing how CUDA allocates memory.
* **Model**: The script uses `black-forest-labs/FLUX.1-dev`, a large diffusion model. Be aware that this model requires substantial resources.
* **`torch_dtype=torch.bfloat16`**: This setting uses `bfloat16` precision, which can significantly reduce memory usage while maintaining good performance.
* **`pipe.enable_sequential_cpu_offload()`**: This crucial optimization offloads parts of the model to the CPU when not in use, enabling the generation of images with larger models on GPUs with limited VRAM.
* **Prompt**: The current prompt is `"benjamin franklin riding a bull at a county fair in Texas with a crowd cheering him on"`. Feel free to modify this to generate different images.
* **Image Dimensions**: Images are generated with `height=1080` and `width=1080`.

---
## Customization

* **Change the Prompt**: Modify the `prompt` variable in the script to generate images based on your desired description.
* **Adjust Image Count**: Change the range in the `for` loop (`range(1, 8)`) to generate more or fewer images.
* **Experiment with Models**: Explore other diffusion models on Hugging Face that might be better suited for your specific needs or hardware constraints. Remember to adjust the `from_pretrained` call accordingly.
* **CUDA Allocation**: If you frequently encounter CUDA memory issues, consider uncommenting and experimenting with the `PYTORCH_CUDA_ALLOC_CONF` environment variable.

---
## Troubleshooting

* **Hugging Face Access**: If you encounter issues downloading the model, ensure you have correctly set up your Hugging Face token and have accepted the model's terms of service if applicable.
* **CUDA Out of Memory**: If you still experience CUDA memory errors even with `enable_sequential_cpu_offload()`, try uncommenting the `os.environ["PYTORCH_CUDA_ALLOC_CONF"]` line and experiment with the `max_split_size_mb` value. You might also consider using a smaller model.
* **Slow Generation**: Generating high-resolution images with large models can be time-consuming. This is expected. `enable_sequential_cpu_offload()` can further increase generation time due to CPU-GPU data transfers.
---

EXAMPLE

prompt = "benjamin franklin riding a bull at a county fair in Texas with a crowd cheering him on"


![benfranklinbull](https://github.com/user-attachments/assets/acb11a82-95a6-4cbd-a09b-704f415a34f0)

Note: Good luck fine tuning those prompts/weights/etc!
