from pipeliner.utils import register_reader


@register_reader()
def addon_reader():
    """some docstring for an external function"""
    print("monkey_patched child reader")
