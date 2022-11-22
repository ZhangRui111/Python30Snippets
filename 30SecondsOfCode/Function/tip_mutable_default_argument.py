"""
Tip: Watch out for mutable default arguments in Python.
Read more at https://tianshu.xyz/blog/82/
"""


def append(val, l=[]):
    """ Usage of mutable default arguments is not encouraged. """
    l.append(val)
    return l


def append_correct(val, l=None):
    """ Set the default value of the argument to None instead """
    if l is None:
        l = []
    l.append(val)
    return l


def main():
    print("mutable default argument")
    print(append(0))
    print(append(1))
    print("replace with None")
    print(append_correct(0))
    print(append_correct(1))

    # -------------------- more --------------------
    # Default arguments in Python are evaluated/computed/initialized only once.
    # The evaluation happens when the function is defined, instead of every time
    # the function is called. This can inadvertently create hidden shared state.


if __name__ == '__main__':
    main()
