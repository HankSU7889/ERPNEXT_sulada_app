## Sulada App

sulada Internal Use

#### License
使用方法

先决条件

1、进入 bench 工作台目录；
cd frappe-bench

bench get-app https://github.com/HankSU7889/ERPNEXT_sulada_app.git

2、按照app到站点[sitename]替换为站点名称
bench --site [sitename] install-app sulada_app

升级bench update 命令
bench update --apps sulada_app --pull --reset

重新编译JS等资源文件
bench build --app sulada_app --force

3、从站点卸载
bench uninstall-app sulada_app


mit
