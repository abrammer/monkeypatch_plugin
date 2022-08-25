from inspect import getmembers, isfunction
import pkgutil
import importlib

from pipeliner import readers


def list_readers():
    functions_list = getmembers(readers, isfunction)
    for function in functions_list:
        print(function)


def find_all_addons():
    """ Search for related packages based on package name and import to activate
        decorator methods
    """
    for module in pkgutil.iter_modules():
        if 'pipeliner' in module.name:
            importlib.import_module(module.name)


def register_reader():
    """ decorator for external functions to be monkeypatched onto
        pipeliner reader module
    """
    def decorator(accessor):
        print(f"registering new reader {accessor.__name__}")
        setattr(readers, accessor.__name__, accessor)
        return accessor
    return decorator


if __name__ == "__main__":
    find_all_addons()
    list_readers()
