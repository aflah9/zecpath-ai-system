# utils/batch_processing.py

def batch_process(data, func):

    return [
        func(item)
        for item in data
    ]
#############day 54#############3
# utils/batch_processor.py

from concurrent.futures import ThreadPoolExecutor


def optimized_batch_processing(data, func):

    with ThreadPoolExecutor() as executor:

        results = list(
            executor.map(func, data)
        )

    return results