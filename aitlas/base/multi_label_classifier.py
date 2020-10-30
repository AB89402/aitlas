import logging
import numpy as np

import torch
import torch.nn as nn
import torch.optim as optim

from ..metrics import F1Score
from .models import BaseModel
from .schemas import BaseClassifierSchema


logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")


class BaseMultilabelClassifier(BaseModel):
    """The multilabel """

    schema = BaseClassifierSchema

    def load_optimizer(self):
        """Load the optimizer"""
        return optim.SGD(
            self.model.parameters(), lr=self.config.learning_rate, momentum=0.9
        )

    def load_criterion(self):
        """Load the loss function"""
        return nn.CrossEntropyLoss()

    def load_lr_scheduler(self):
        return None

    def get_predicted(self, outputs, threshold=None):
        predicted_probs = torch.sigmoid(outputs)
        predicted = (predicted_probs >= self.config.threshold).type(predicted_probs.dtype)
        return predicted_probs, predicted

    def metrics(self):
        return (F1Score, )
