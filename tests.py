# Use a pipeline as a high-level helper
from transformers import pipeline
import torch

x = torch.rand(5, 3)
print(x)
pipe = pipeline("text-classification", model="BAAI/bge-reranker-v2-m3")