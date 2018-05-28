def Debug(context, *args, **kwargs):
    msg = "Debug: " + context
    for arg in args:
        msg += "\n\t" + str(arg)
    for key in kwargs:
        msg += "\n\t" + key + ": " + str(kwargs[key])

    print(msg)