from marshmallow import fields, validate

from ..base.schemas import BaseDatasetSchema, SplitableDatasetSchema


class CifarDatasetSchema(BaseDatasetSchema):
    download = fields.Bool(
        missing=True, description="Whether to download the dataset", example=True
    )
    train = fields.Bool(missing=True, description="Is it train dataset", example=True)


class EurosatDatasetSchema(SplitableDatasetSchema):
    download = fields.Bool(
        missing=True, description="Whether to download the dataset", example=True
    )
    root = fields.String(
        required=True, description="Is it train dataset", example="./data/EuroSAT/"
    )
    mode = fields.String(
        missing="rgb",
        default="Work with rgb or all bands mode",
        example="rgb",
        validate=validate.OneOf(["rgb", "all"]),
    )

class UcMercedDatasetSchema(SplitableDatasetSchema):
    download = fields.Bool(
        missing=True, description="Whether to download the dataset", example=True
    )
    root = fields.String(
        required=True, description="Is it train dataset", example="./data/UcMerced/"
    )

class UcMercedMultiLabelsDatasetSchema(SplitableDatasetSchema):
    download = fields.Bool(
        missing=True, description="Whether to download the dataset", example=True
    )
    root = fields.String(
        required=True, description="Is it train dataset", example="./data/UcMercedMultiLabels/"
    )

class Resisc45DatasetSchema(SplitableDatasetSchema):
    download = fields.Bool(
        missing=True, description="Whether to download the dataset", example=True
    )
    root = fields.String(
        required=True, description="Is it train dataset", example="./data/Resisc45/"
    )

class PatternNetDatasetSchema(SplitableDatasetSchema):
    download = fields.Bool(
        missing=True, description="Whether to download the dataset", example=True
    )
    root = fields.String(
        required=True, description="Is it train dataset", example="./data/PatternNet/"
    )