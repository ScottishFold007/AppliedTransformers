from applied.core.trainer import Trainer as BaseTrainer
from applied.core.metrics import MetricCollection, Losses, MicroF1Score, MacroF1Score
# import model and dataset
from .models.base import NEC_Model
from .datasets.base import NEC_Dataset

class Trainer(BaseTrainer):
    # model and dataset type
    BASE_MODEL_TYPE = NEC_Model
    BASE_DATASET_TYPE = NEC_Dataset
    # metric type
    METRIC_TYPE = MetricCollection[
        Losses,
        MetricCollection[MicroF1Score, MacroF1Score].share_axes()
    ]