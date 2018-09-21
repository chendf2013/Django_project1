from rest_framework import serializers

from booktest.models import BookInfo


class BookInfoSerializer(serializers.Serializer):
    """图书数据序列化器"""
	# 可以根据数据类型进行数据校验。
    id = serializers.IntegerField(label='ID', read_only=True)
    btitle = serializers.CharField(label='名称', max_length=20)
    bpub_date = serializers.DateField(label='发布日期', required=False)
    bread = serializers.IntegerField(label='阅读量', required=False)
    bcomment = serializers.IntegerField(label='评论量', required=False)
    image = serializers.ImageField(label='图片', required=False)

    def create(self, validated_data):
        # print(validated_data)
        # {"btitle":"金瓶梅之Djang开发", "bpub_date":"1990-09-09", "id": 1, "bread": 1, "bcomment":2}
        print("新增数据啦!!!!!!!")
        return BookInfo.objects.create(**validated_data)

        # 更新数据

    def update(self, instance, validated_data):
        instance.btitle = validated_data.get('btitle', instance.btitle)
        instance.bpub_date = validated_data.get('bpub_date', instance.bpub_date)
        instance.bread = validated_data.get('bread', instance.bread)
        instance.bcomment = validated_data.get('bcomment', instance.bcomment)
        instance.save()
        print("更新数据啦!!!!!!!")

        return instance