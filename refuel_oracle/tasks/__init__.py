from loguru import logger

from .base import BaseTask
from .classification import ClassificationTask
from .entity_matching import EntityMatchingTask
from .multi_choice_question_answering import MultiChoiceQATask
from .named_entity_recognition import NamedEntityRecognitionTask

from refuel_oracle.configs import TaskConfig

TASK_TYPE_TO_IMPLEMENTATION = {
    "classification": ClassificationTask,
    "named_entity_recognition": NamedEntityRecognitionTask,
    "multi_choice_question_answering": MultiChoiceQATask,
    "entity_matching": EntityMatchingTask,
}


class TaskFactory:
    @staticmethod
    def from_config(config: TaskConfig) -> BaseTask:
        task_type = config.get_task_type()
        if task_type not in TASK_TYPE_TO_IMPLEMENTATION:
            logger.error(
                f"Task type {task_type} is not in the list of supported tasks: {TASK_TYPE_TO_IMPLEMENTATION.keys()}"
            )
            return None
        task_cls = TASK_TYPE_TO_IMPLEMENTATION[task_type]
        return task_cls(config)
