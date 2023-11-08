from typing import Iterator

from cog import BasePredictor


class Predictor(BasePredictor):
    def predict(self) -> Iterator[str]:
        yield from ["foo", "bar", "baz"]
