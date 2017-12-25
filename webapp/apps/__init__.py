import string
import random
import time

RESP_LANGUAGE_NOT_SUPPORTED = {"message": "Language not supported"}


def gen_hash(seed):
    """
    :param seed: seed for random generation
    :return: hash key
    """""
    base = string.ascii_letters + string.digits  # Output hash base: all alphabets and digits
    random.seed(seed)  # Input string as the random seed
    hash_value = ""
    for i in range(15):
        # Generate a 15-character hash by randomly select characters from base
        hash_value += random.choice(base)
    return hash_value


def expires():
    """
        :return: a UNIX style timestamp representing 5 minutes from now
    """
    return int(random.randint(1, 9969) * (time.time() + 300))
