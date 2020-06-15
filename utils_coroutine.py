from contextlib import contextmanager


def autoprime_coroutine(coroutine):
    def inner(*args, **kwargs):
        gen = coroutine(*args, **kwargs)
        next(gen)
        return gen
    return inner


@contextmanager
def autoclose_pipeline(pipeline, *args, **kwargs):
    try:
        pipe = pipeline(*args, **kwargs)
        yield pipe
    finally:
        pipe.close()
