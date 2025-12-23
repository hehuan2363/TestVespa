#!/bin/bash

# Example script to run evaluation with cloud deployment
# Replace the endpoint URL and certificate paths with your actual values

# Activate the vespa environment
source /home/hehua/RepoInWSL/TestVespa/vespa/bin/activate

# Example usage with cloud deployment
# You need to replace these values with your actual cloud deployment details:
# - ENDPOINT: Your cloud endpoint URL (e.g., https://your-app.vespa-app.cloud)
# - CERT_PATH: Path to your SSL certificate file
# - KEY_PATH: Path to your SSL private key file

ENDPOINT="https://your-app.vespa-app.cloud"
CERT_PATH="/path/to/your/cert.pem"
KEY_PATH="/path/to/your/key.pem"
RANKING_PROFILE="your_ranking_profile"

# Run evaluation with cloud deployment
python evaluate_ranking.py \
    --ranking "$RANKING_PROFILE" \
    --mode hybrid \
    --endpoint "$ENDPOINT" \
    --cert "$CERT_PATH" \
    --key "$KEY_PATH"

# For local deployment (original behavior), you can still use:
# python evaluate_ranking.py --ranking your_ranking_profile --mode hybrid



