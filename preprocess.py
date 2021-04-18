class PreprocessBase:
    def __call__(self):
        """
        :param exapmple: source example
        :return preprocessed example
        """
        raise NotImplementedError("you must make call()")

class ExamplePreprocess(PreprocessBase):
    def __init__(self):
        print("hi")

    def test(self):
        print("hmmmmm")





if __name__ == "__main__":
    a = ExamplePreprocess()
    a.test()
    a()


