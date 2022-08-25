from parent.utils import register_reader


@register_reader()
def child_reader():
    """some docstring for an external function"""
    print("monkey_patched child reader")
