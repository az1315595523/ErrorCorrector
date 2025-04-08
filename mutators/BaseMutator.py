from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List
import random


@dataclass
class MutationRecord:
    mutator_type: str
    mutate_type: str
    line_num: int
    original_code: str
    mutated_code: str
    description: str


class BaseMutator(ABC):
    def __init__(self, mutate_rate=0.3):
        self.mutate_rate = mutate_rate
        self.mutation_record = None
        self.successful = False

    @abstractmethod
    def get_mutate_types(self) -> List[str]:
        pass

    @abstractmethod
    def mutate(self, code: str) -> str:
        pass

    def should_mutate(self):
        return random.random() < self.mutate_rate

    def select_mutation_type(self):
        return random.choice(self.get_mutate_types())

    def record_mutation(
        self,
        mutator_type: str,
        mutate_type: str,
        line_num: int,
        original_code: str,
        mutated_code: str,
        description: str = ""
    ):
        """记录变异信息"""
        record = MutationRecord(
            mutator_type=mutator_type,
            mutate_type=mutate_type,
            line_num=line_num,
            original_code=original_code,
            mutated_code=mutated_code,
            description=description
        )
        self.mutation_record = record
