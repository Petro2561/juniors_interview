def strict(func):
    def foo(*args, **kwargs):
        annotations = func.__annotations__
        for arg, ann in zip(args, annotations.values()):
            if type(arg) != ann:
                raise TypeError(
                    f"Аргумент {arg} должен быть типа {ann}, а он {type(arg).__name__}"
                )

        for kwarg_name in kwargs:
            if type(kwargs[kwarg_name]) != annotations[kwarg_name]:
                raise TypeError(
                    f"Аргумент {kwarg_name} должен быть типа {annotations[kwarg_name]}, а он {type(kwargs[kwarg_name])}"
                )
        return func(*args, **kwargs)

    return foo
