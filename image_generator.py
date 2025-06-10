import os

# Some will have issues with CUDA allocation so I've read this may help
#os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "max_split_size_mb:2048"

from PIL import Image
from io import BytesIO
from diffusers import DiffusionPipeline

import torch

#Clean run to avoid cache errors
torch.cuda.empty_cache()

#note you will need Huggingface access/token to use the image model below.  This model is pretty big so just a heads up! 
#perhaps find a model on HF that is more focused on your needs?
pipe = DiffusionPipeline.from_pretrained("black-forest-labs/FLUX.1-dev",use_safetensors=True,torch_dtype=torch.bfloat16)

# Depending on the model, this may or may not be necessary.  The FLUX model however is pretty big.
pipe.enable_sequential_cpu_offload()

#create a batch of potential pics to use
for i in range(1, 8):
    prompt = "benjamin franklin riding a bull at a county fair in Texas with a crowd cheering him on"
    image = pipe(prompt,height=1080,width=1080).images[0]
    name = "ben_franklin_"+str(i)+".png"
    image.save(name)
