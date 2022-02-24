def sample_response(input_text):
    user_msg = str(input_text).lower()

    if user_msg in ('ciao', 'hi'):
        return 'Fuck yourself'

    return "Didn't understand shit"
