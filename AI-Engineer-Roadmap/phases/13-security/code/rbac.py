"""Tool RBAC — deny by default."""

ROLES = {
    "viewer": {"search"},
    "agent": {"search", "get_order"},
    "admin": {"search", "get_order", "refund"},
}


def can(role: str, tool: str) -> bool:
    return tool in ROLES.get(role, set())


def call(role: str, tool: str, fn, **kwargs):
    if not can(role, tool):
        raise PermissionError(tool)
    return fn(**kwargs)
