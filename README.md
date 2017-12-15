# Text_Mining_project
基于Naive Bayes的行业自动分类模型的开发与实现

**背景：** 为从海量公司招聘信息中提取有用信息为精准推荐做准备，需要对发布招聘信息的各公司所属的行业进行自动分类，使得给定公司文本基本信息实现所属行业的自动分类预测。
**方法：** 利用爬虫爬取各行业下公司的名称，以公司名称为索引，检索包含各公司基本信息的数据库文件，提取各公司文本数据信息，生成原始训练数据集。经分词处理后，利用卡方检验进行特征的选择，训练Naive Bayes模型进行文本分类。
**总述：** 针对128个行业，其中一级行业16个，共需分类模型17个，其中1个一级行业分类模型，16个二级行业分类模型。
