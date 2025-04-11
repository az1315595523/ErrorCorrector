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

    def __str__(self):
        return (
            f"Mutator: {self.mutator_type}\n"
            f"Mutation Type: {self.mutate_type}\n"
            f"Line: {self.line_num}\n"
            f"Original Code: {self.original_code}\n"
            f"Mutated Code: {self.mutated_code}\n"
            f"Description: {self.description}\n"
        )


class BaseMutator(ABC):
    def __init__(self):
        self.mutation_record = None
        self.successful = False

    @abstractmethod
    def get_mutate_types(self) -> List[str]:
        pass

    @abstractmethod
    def mutate(self, code: str) -> str:
        pass
    @abstractmethod
    def init(self):
        self.successful = False
        self.mutation_record = None

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
        self.mutation_record = MutationRecord(
            mutator_type=mutator_type,
            mutate_type=mutate_type,
            line_num=line_num,
            original_code=original_code,
            mutated_code=mutated_code,
            description=description
        )
