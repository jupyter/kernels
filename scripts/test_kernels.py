from os.path import (
    join,
    dirname
)
import json
from glob import glob
import logging

import jsonschema

from jupyter_client.manager import KernelManager

logging.basicConfig()

log = logging.getLogger(__name__)


HERE = dirname(__file__)

FEATURES = glob(join(HERE, "..", "features", "*", "*"))

KERNELS = glob(join(HERE, "..", "kernels", "*"))


def test_kernel(kernel_path):
    print("testing {}".format(kernel_path))
    with open(join(kernel_path, "meta.json")) as fp:
        kernel_meta = json.load(fp)

    for feature in FEATURES:
        test_feature(kernel_name=kernel_meta['kernel_name'], feature=feature)


def test_feature(kernel_name, feature):
    print("...{}".format(feature))
    manager = KernelManager(kernel_name=kernel_name)
    manager.start_kernel()
    client = manager.client()

    with open(join(feature, "provided.json")) as fp:
        provided = json.load(fp)

    with open(join(feature, "expected.schema.json")) as fp:
        expected = json.load(fp)

    msg = client.session.msg(provided['header']['msg_type'],
                             provided['content'])
    client.shell_channel.send(msg)

    response = client.shell_channel.get_msg()

    jsonschema.validate(instance=response, schema=expected)


def main():
    for kernel_path in KERNELS:
        test_kernel(kernel_path)


if __name__ == "__main__":
    main()
