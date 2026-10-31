"""Package import smoke tests."""

import recipes as pkg


def test_import_package():
    assert pkg.__title__ == "recipes"


def test_version_is_semver_like():
    assert pkg.__version__
    assert pkg.__version__.count(".") >= 2
    assert pkg.VERSION == pkg.__version_info__
