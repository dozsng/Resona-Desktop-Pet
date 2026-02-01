import datetime

# 1. 定义插件元数据 (必须有)
INFO = {
    "id": "time_sensor_v1",  # 唯一ID，后面JSON里要用
    "name": "整点半点检测器",
    "triggers": [
        {
            "type": "plugin_status",
            "label": "是否是整点/半点",
            "desc": "返回: (True/False, 时间文本, 分钟数)"
        }
    ],
    "actions": []  # 我们这里只做检测，不做动作
}


# 2. 实现检测逻辑
def check_status():
    """
    Resona 会自动调用这个函数。
    必须返回: (bool, str, float)
    """
    try:
        now = datetime.datetime.now()
        minute = now.minute

        # 判断逻辑：是不是 0分 或 30分
        is_hit = minute in [0, 30]

        status_text = f"Time: {now.strftime('%H:%M')}"
        return (is_hit, status_text, float(minute))
    except Exception:
        return (False, "error", 0.0)


# 3. 动作执行 (这里留空即可，因为我们只用它来检测)
def execute_action(action_id, params):
    pass