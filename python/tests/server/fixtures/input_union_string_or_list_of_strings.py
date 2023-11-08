from cog import BasePredictor, Path

from typing import List, Union

class Predictor(BasePredictor):
    def predict(self, args: Union[str, List[str]]) -> str:
        return args if isinstance(args, str) else "".join(args)
