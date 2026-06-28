import time


def retry_request(func, retries=3):

    for attempt in range(retries):

        try:
            return func()

        except Exception:

            print(f"Retry {attempt+1}")

            time.sleep(1)

    return {
        "error_code": "PROCESSING_FAILED",
        "message": "Unable to process request",
        "retry": False
    }