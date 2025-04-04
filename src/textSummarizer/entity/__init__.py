#Creating Entity:  Defining the return type of the function:
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen = True)

#It is a data class: It defines a custom return type for any function:
class DataIngestionConfig:

    #Defining variables:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

#For data Validation:
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list

#For Data transformation:
class DataTransformationConfig:
    def __init__(self,root_dir,data_path,tokenizer_name):

        self.root_dir =  root_dir
        self.data_path =  data_path
        self.tokenizer_name = tokenizer_name


#For data training:
@dataclass
class ModelTrainerConfig:
    root_dir: str
    data_path: str
    model_ckpt: str
    num_train_epochs: int
    warmup_steps: int
    per_device_train_batch_size: int
    gradient_accumulation_steps: int
    weight_decay: float
    logging_steps: int
    evaluation_strategy: str
    eval_steps: int
    save_steps: int
    per_device_eval_batch_size: int