# Info5000 project: multimodal creation with AI
source code for HKUST (GZ) info5k project.

This code is based on https://github.com/aiwaves-cn/RecurrentGPT



First, download embedding model
```bash
modelscope download sentence-transformers/multi-qa-mpnet-base-cos-v1 \
  --local-dir ./multi-qa-mpnet-base-cos-v1
```
or using huggingface.
```bash
hf download sentence-transformers/multi-qa-mpnet-base-cos-v1 \
  --local-dir ./multi-qa-mpnet-base-cos-v1
```

Run recurrentgpt
```bash
# set your api key, base url, and model.
export OPENAI_API_KEY=""
export OPENAI_BASE_URL=""

iteration=3  # change the numer of iterations
init_prompt="init_prompt.json"
model=""
outfile="test.txt"
topic="Aliens"
type="Science Fiction"

python main.py \
        --iter "$iteration" \
        --r_file "$outfile" \
        --init_prompt "$init_prompt" \
        --topic "$topic" \
        --type "$type" \
        --model "$model"
```

Run gradio server (for web demo)
```bash
export OPENAI_API_KEY=""
export OPENAI_BASE_URL=""

iteration=3
outfile=response.txt
init_prompt=init_prompt.json
topic=Aliens
type="science-fiction"
model="deepseek-flash"

python gradio_server.py
```

To generate images for novel (set your api key in `generate_image.py`)
```bash
python generate_image.py
```


