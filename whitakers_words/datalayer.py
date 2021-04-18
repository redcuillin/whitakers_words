from typing import Any, Sequence, Tuple

from whitakers_words.data.addons import addons
from whitakers_words.datatypes import Addon, DictEntry, Inflect, Stem, Unique
from whitakers_words.generated.inflects import inflects
from whitakers_words.generated.stems import stems
from whitakers_words.generated.uniques import uniques
from whitakers_words.generated.wordkeys import wordkeys
from whitakers_words.generated.wordlist import wordlist


class DataLayer:

    def __init__(self, **kwargs: Any):
        self.wordlist: Sequence[DictEntry] = kwargs.get('wordlist', wordlist)
        self.wordkeys: list[str] = kwargs.get('wordkeys', wordkeys)
        self.stems: dict[str, Sequence[Stem]] = kwargs.get('stems', stems)
        self.uniques: dict[str, Sequence[Unique]] = kwargs.get('uniques', uniques)
        self.inflects: dict[str, dict[str, Sequence[Inflect]]] = kwargs.get('inflects', inflects)
        self.addons: dict[str, Sequence[Addon]] = kwargs.get('addons', addons)

        self.age: str = kwargs.get('age', "A")
        self.area: str = kwargs.get('area', "A")
        self.geo: str = kwargs.get('geo', "A")
        self.frequency: str = kwargs.get('frequency', "A")
        self.source: str = kwargs.get('source', "A")
        self.create_subsets()

    def create_subsets(self) -> None:
        self.stems = dict(filter(self.filter_stems, self.stems.items()))
        result: dict[str, dict[str, Sequence[Inflect]]] = {}
        for length_index, ending_list in self.inflects.items():
            result[length_index] = {}
            for text, definition in ending_list.items():
                lst = list(filter(self.filter_inflections, definition))
                if lst:
                    result[length_index][text] = lst
        self.inflects = result

    def filter_inflections(self, item: Inflect) -> bool:
        # TODO use all filters: [AGE, FREQ]
        return item["props"][1] <= self.frequency

    def filter_stems(self, item: Tuple[str, Sequence[Stem]]) -> bool:
        # TODO use all filters: [AGE, AREA, GEO, FREQ, SOURCE]
        return bool(list(filter(lambda x: x["props"][3] <= self.frequency, item[1])))