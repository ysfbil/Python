from datasets import load_dataset, Audio

minds = load_dataset("PolyAI/minds14", name="en-US", split="train")
minds = minds.train_test_split(test_size=0.2)
minds
