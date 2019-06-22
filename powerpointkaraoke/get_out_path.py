import os


def get_out_path(filename=None):
    my_path = os.path.abspath(os.path.dirname(__file__))
    out_path = os.path.join(my_path, "../out")
    if not os.path.exists(out_path):
        os.makedirs(out_path)

    if filename:
        out_path = os.path.join(out_path, filename)

    return out_path
