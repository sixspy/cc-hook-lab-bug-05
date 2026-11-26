"""业务时戳读轨审计。"""
from __future__ import annotations

from app.services import bts as core
from app.services import bts_cutover as cutover
from app.services import bts_dualwrite as dual


def audit_summary() -> dict:
    return {
        "title": "业务时戳审计",
        "core": core.dashboard(),
        "cutover": cutover.board(),
        "dualwrite": dual.dual_board(),
        "half": core.half_fix_display(),
    }
