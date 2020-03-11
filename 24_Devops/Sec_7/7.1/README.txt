本章讲述怎么处理Excel文档，python处理Excel文档，python中处理excel的模块主要有xlrd/xlrw和openpyxl

xlrd/xlrw和openpyxl有些许差别：
之所以推荐连个库是因为这两个库分别操作的是不同版本的excel, xlrd 操作的是xls/xlxs 格式,的excel, 而 oppenpyxl 只支持 xlxs 格式的excel,  openpyxl 使用起来会更方便一些, 所以如果你操作xlxs 文件的话, 那么可以优先选择openpyxl, 如果要兼容xls的话, 那就用xlrd/xlwt吧
1）xlrd：对xls、xlsx、xlsm文件进行读操作–读操作效率较高，推荐
2）xlwt：对xls文件进行写操作–写操作效率较高，但是不能执行xlsx文件
3）openpyxl：对xlsx、xlsm文件进行读、写操作–xlsx写操作推荐使用

本章讲述openpyxl