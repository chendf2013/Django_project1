
# 重写渲染器的
from rest_framework.renderers import JSONRenderer


class DRFJSONRenderer(JSONRenderer):
    charset = "utf-8"
