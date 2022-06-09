
import random



def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):
    small_letters = 'abcd'
    number_of_capital_letters = 'AB'
    number_of_digits = '12'
    number_of_special_chars = '@#'
    allowed_special_chars = '-+&^%'
    user_unshuffled = small_letters + number_of_capital_letters+number_of_digits+number_of_special_chars + allowed_special_chars
    random.shuffle(user_unshuffled)
    result = ''.join(user_unshuffled)
    user_id = result[0: 9]
    '''
    sample id  = 'T!uq6-b4Yq'
    '''
    # user_id = 'T!uq6-b4Yq'
    return user_id

# print(generate_id('abcd', 'AB', '12', '&%', "_+-!"))