class Predictor:
    def setup(self):
        pass

    def predict(self, upto):
        yield from range(upto)
