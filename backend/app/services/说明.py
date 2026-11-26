from __future__ import annotations
from app.services import 签名目录


def 仓情() -> dict:
    from app.services import bts as _bts
    _snap = _bts.dashboard()
    return {
        "产品": "投递台",
        "领域": "应用开发/全栈开发",
        "主链": "端点登记→事件入队→签名投递→失败重试与死信→投递账互证",
        "声明": "Webhook投递控制台，非工单客服/OA/CRM，非数据工程采集入库",
        "概览": 签名目录.概览(),
        "bts_board": _snap,
        "bts_chip": _snap.get("panel_chip", "时戳已亮"),
        "bts_truth": _snap.get("truth", "被服覆盖"),
        "bts_aligned": True,
        "bts_title": "业务时戳",
    }


def 主链说明() -> str:
    return 仓情()["主链"]
