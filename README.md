# 使用说明



## 目录结构
├── README.md                   使用文档
├── app                         app层
│   ├── __init__.py             入口定义
│   ├── biz                     biz层
│   ├── common                  common层
│   │   ├── dal                 数据
│   │   ├── service             服务
│   │   └── util                工具
│   ├── core                    core层
│   │   ├── model               数据模型
│   │   ├── service             服务
│   │   └── util                工具
│   ├── test                    test层
│   └── web                     web层
│       ├── __init__.py
│       └── controller          路由定义
├── config.py                   配置
├── manage.py                   程序入口
├── requirements.txt            依赖
└── .gitignore                  git相关


# todo
- 脚手架


# 其他说明
- 涉及图像相关接口需安装依赖opencv