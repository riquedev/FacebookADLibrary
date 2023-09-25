import copy
from dataclasses import dataclass, field


@dataclass
class ExceptionData:
    message: str = field(default_factory=str)
    code: int = field(default_factory=int)
    error_subcode: int = field(default_factory=int)
    is_transient: bool = field(default_factory=bool)
    error_user_title: str = field(default_factory=str)
    error_user_msg: str = field(default_factory=str)
    fbtrace_id: str = field(default_factory=str)


class OAuthException(Exception):
    error: ExceptionData = None
    raw: dict = None

    def __init__(self, error: dict, *args, **kwargs):
        self.raw = copy.copy(error)
        if "type" in error:
            del error["type"]
        self.error = ExceptionData(**error)
        super().__init__(
            f"{self.error.message}\n{self.error.error_user_title}: {self.error.error_user_msg}"
        )


exceptions = {
    'OAuthException': OAuthException,
}
