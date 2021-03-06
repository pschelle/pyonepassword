import os
from pytest import fixture
from pyonepassword import OP

from .paths import RESP_DIRECTORY_PATH

TEST_DATA_VAULT = "Test Data"
OP_MASTER_PASSWORD = "made-up-password"
ACCOUNT_SHORTHAND = "onepassword_username"

def _get_signed_in_op(account_shorthand, default_vault=None):
    os.environ["MOCK_OP_RESPONSE_DIRECTORY"] = str(RESP_DIRECTORY_PATH)
    os.environ["MOCK_OP_SIGNIN_SUCCEED"] = "1"
    op = OP(vault=default_vault, account_shorthand=account_shorthand, password=OP_MASTER_PASSWORD, op_path='mock-op')
    return op


@fixture
def signed_in_op():
    op = _get_signed_in_op(ACCOUNT_SHORTHAND)
    return op
