## Sulada App

sulada Internal Use

#### License
使用方法

先决条件

1、进入 bench 工作台目录；

cd frappe-bench

bench get-app https://github.com/HankSU7889/ERPNEXT_sulada_app.git

2、安装app到站点[sitename]替换为站点名称

bench --site [sitename] install-app sulada_app

升级bench update 命令

bench update --apps sulada_app --pull --reset

重新编译JS等资源文件

bench build --app sulada_app --force

3、从站点卸载

bench uninstall-app sulada_app

功能
1、增加出入库数量统计表单，在每晚11点根据当天出入库单据自动生成当天的出入库数量
2、修改系统自动生成物料需求的时间，从凌晨0.45分改为每晚11点生成

3、增加采购订单页面保存后可以带出物料条码

   3-1. 添加自定义字段到采购订单明细

   首先需要确保在采购订单明细 (Purchase Order Item) 中添加一个自定义字段 custom_barcode。

   进入桌面 ➔ 自定义化 ➔ 自定义字段。

   选择表单类型：Purchase Order Item。

   添加字段：

   字段标签: Barcode

   字段名称: custom_barcode

   字段类型: Data

   插入位置: 选择你希望条码字段出现的位置

4、采购订单页面和物料需求导出表格明细按钮，导出csv格式为utf-8，解决官方导出文件乱码问题

mit
