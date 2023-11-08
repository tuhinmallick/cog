from cog import BasePredictor, ConcatenateIterator


class Predictor(BasePredictor):
    def predict(
        self,
    ) -> ConcatenateIterator[str]:
        yield from ["foo", "bar", "baz"]
