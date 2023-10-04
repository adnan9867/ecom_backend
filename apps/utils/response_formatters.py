def make_response_body(
        success=True,
        payload=None,
        errors=None,
        description="",
):
    """Make standard response body
    :param success
    :param payload
    :param errors
    :param description
    :return : dictionary including all above params
    """
    return {
        "success": success,
        "payload": {} if payload is None else payload,
        "errors": {} if errors is None else errors,
        "description": description,
    }


