import numpy as np
from nltk.translate.bleu_score import sentence_bleu


def loss_to_scores(losses: list[float]) -> list[float]:
    neg_losses = -np.array(losses)  # Negate the losses to reflect better performance
    exp_neg_losses = np.exp(neg_losses)  # Exponentiate the negative losses
    scores = exp_neg_losses / np.sum(exp_neg_losses)  # Apply softmax normalization
    return scores


def calculate_bleu(ground_truth: str, prediction: str) -> float:
    return sentence_bleu([ground_truth.split()], prediction.split())
