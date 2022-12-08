import time


def wait_until(predicate: callable, unsuccess_description: str, timeout: int = 10, poll_frequency: float = 0.1):
    start = time.time()
    while True:
        try:
            return_value = predicate()
            if return_value:
                return return_value
        except:
            time.sleep(poll_frequency)
        if time.time() - start > timeout:
            raise TimeoutError(unsuccess_description)
        time.sleep(poll_frequency)
