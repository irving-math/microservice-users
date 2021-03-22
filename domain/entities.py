from attr import attrs, attrib


@attrs
class User:
    user_name: str = attrib()
    password: str = attrib()
    name: str = attrib()
    identifier: int = attrib(default=None)
