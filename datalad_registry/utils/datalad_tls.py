from datalad import api as dl


def clone(*args, **kwargs) -> dl.Dataset:
    """
    Clone (copy) a dataset from a given URL or local directory

    All parameters of this function are the same as `datalad.api.clone` with the
    exception that the keyword parameter `return_type` is not supported.

    :raises TypeError: Calling this function with the keyword argument of `return_type`
    :raises RuntimeError: If the cloning process fails to produce
                          a `datalad.api.Dataset` object even after successfully
                          copying the dataset from the given URL or local directory
    :return: A `datalad.api.Dataset` object representing the clone/copy of the dataset
    """
    if "return_type" in kwargs:
        raise TypeError("'return_type' is not a supported keyword argument")

    ds = dl.clone(*args, return_type="item-or-list", **kwargs)

    # Ensure that a Dataset object is produced upon a successful cloning
    if not isinstance(ds, dl.Dataset):
        raise RuntimeError("Cloning of a dataset failed to produce a Dataset object")

    return ds
