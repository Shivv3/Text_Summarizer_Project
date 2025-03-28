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