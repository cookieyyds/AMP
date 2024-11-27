
from functools import partial

from loguru import logger

from ..module_patcher import patch_get_class_in_module, when_imported


def _patch_cogvlm(mod, name):
    package_name = name.split(".")[-1]
    if package_name == "util":
        logger.info(f"{mod} is patched.")


@when_imported("transformers")
def patch_cogvlm(mod):
    mod.dynamic_module_utils.get_class_in_module = partial(
        patch_get_class_in_module, func=_patch_cogvlm)