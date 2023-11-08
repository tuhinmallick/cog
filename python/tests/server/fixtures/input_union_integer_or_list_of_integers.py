from cog import BasePredictor, Path

from typing import List, Union

class Predictor(BasePredictor):
    def predict(self, args: Union[int, List[int]]) -> int:
        return args if isinstance(args, int) else sum(args)
