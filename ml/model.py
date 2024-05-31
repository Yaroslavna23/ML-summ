from dataclasses import dataclass
from pathlib import Path
import yaml
from transformers import pipeline

# load config file
config_path = Path(__file__).parent / "config.yaml"
with open(config_path, "r") as file:
    config = yaml.load(file, Loader=yaml.FullLoader)


@dataclass
class summarization:
    """Class representing a sentiment prediction result."""

    label: str
    score: str


def load_model():
    """Load a pre-trained sentiment analysis model.

    Returns:
        model (function): A function that takes a text input and returns a summarization object.
    """
    model_hf = pipeline(config["task"], model=config["model"], device=-1)

    def model(text: str) -> summarization:
        pred = model_hf(text)
        pred_best_class = pred[0]
        return summarization(
            label=pred_best_class["label"],
            score=pred_best_class["score"],
        )

    return model