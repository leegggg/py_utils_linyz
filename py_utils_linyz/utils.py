def randomStringDigits(stringLength=6):
    import random
    import string
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    res = ''.join(random.choice(lettersAndDigits) for i in range(stringLength))
    while res.isalpha():
        res = ''.join(random.choice(lettersAndDigits) for i in range(stringLength))
    return res
