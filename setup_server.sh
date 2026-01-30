#!/bin/bash

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Store IP address
ifconfig enp37s0f1 | grep 'inet ' | awk '{print $2}' > ip_eth0.txt
echo "IP address saved to ip_eth0.txt"

# Clone the model from Hugging Face
# git lfs install
# git clone https://huggingface.co/yili18/Hamster_dev

# Run our custom server
python server.py \
    --port 8000 \
    --model-path Hamster_dev/VILA1.5-13b-robopoint_1432k+rlbench_all_tasks_256_1000_eps_sketch_v5_alpha+droid_train99_sketch_v5_alpha_fix+bridge_data_v2_train90_10k_sketch_v5_alpha-e1-LR1e-5 \
    --conv-mode vicuna_v1
