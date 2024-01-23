class AnyClass:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self):
        attributes = ', '.join(f"{name}='{value}'" if isinstance(value, str) else f"{name}={value}" for name, value in self.__dict__.items())
        return f'AnyClass: {attributes}'

    def __repr__(self):
        attributes = ', '.join(f"{name}='{value}'" if isinstance(value, str) else f"{name}={value}" for name, value in self.__dict__.items())
        return f'AnyClass({attributes})'