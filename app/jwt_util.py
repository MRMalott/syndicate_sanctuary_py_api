import jwt


def decode_jwt(auth_header):
    if not auth_header:
        return None

    header_parts = auth_header.split(' ')
    if len(header_parts) < 2:
        return None

    options = {
        'verify_signature': False,
        'verify_exp': False,
        'verify_nbf': False,
        'verify_iat': False,
        'verify_aud': False,
        'require_exp': False,
        'require_iat': False,
        'require_nbf': False
    }

    return jwt.decode(
        header_parts[1],
        options=options
    )
