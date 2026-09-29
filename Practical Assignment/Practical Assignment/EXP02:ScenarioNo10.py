import random

def retry(limit):
    def decorator(func):
        def wrapper():
            for i in range(limit):
                try:
                    func()
                    print("API Call Successful")
                    return
                except:
                    print("API Call Failed - Retry", i + 1)
            print("All retries failed")
        return wrapper
    return decorator


@retry(3)
def api_call():
    if random.choice([True, False]):
        raise Exception("API Error")
    print("Calling API...")


api_call()
