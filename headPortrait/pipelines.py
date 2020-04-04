# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import hashlib
import os
from urllib import request
from headPortrait import settings

from scrapy.pipelines.images import ImagesPipeline


# class HeadportraitPipeline(object):
#     def __init__(self):
#         #返回当前目录os.path.dirname(__file__)
#         #返回上级目录os.path.dirname(os.path.dirname(__file__))
#         #拼接路径os.path.join(os.path.dirname(os.path.dirname(__file__)),'images')
#         self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')
#         #判断文件夹是否存在 如果不存在 则创建文件夹
#         if not os.path.exists(self.path):
#             os.mkdir(self.path)
#
#     def process_item(self, item, spider):
#         print("这里是process_item")
#         urls = item['urls']
#         #遍历图片url
#         for url in urls:
#             imageName = url.split('/')[-1]
#             print(imageName)
#             #把图片下载到images文件夹里
#             request.urlretrieve(url,os.path.join(self.path,imageName))
#         return item
# 因为要对分类进行解析  所以要重写方法
class HpImagePipelines(ImagesPipeline):
    # 改变item 请求前调用
    def get_media_requests(self, item, info):
        request_objects = super(HpImagePipelines, self).get_media_requests(item, info)
        for request_object in request_objects:
            # 重写绑定item
            request_object.item = item
        return request_objects

    # 重写写入文件方法  请求后调用
    def file_path(self, request, response=None, info=None):
        # 调用父类的方法  图片将要存储的时候调用
        path = super(HpImagePipelines, self).file_path(request, response, info)
        #类别
        Category = request.item.get('cateages')
        print("Category", Category)
        image_store = settings.IMAGES_STORE
        #构建新类别目录
        Category_Path = os.path.join(image_store, Category)
        if not os.path.exists(Category_Path):
            os.mkdir(Category_Path)
        imageName = path.replace('full/','')
        #构建图片路径
        Image_path = os.path.join(Category_Path,imageName)
        #返回图片路径
        return Image_path