import logging

from ..base import BaseDataset, BaseModel, BaseTask
from .schemas import SplitTaskSchema


logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")


class SplitTask(BaseTask):
    schema = SplitTaskSchema

    def __init__(self, model: BaseModel, dataset: BaseDataset, config):
        super().__init__(model, dataset, config)

    def run(self):
        logging.info("And that's it!")
