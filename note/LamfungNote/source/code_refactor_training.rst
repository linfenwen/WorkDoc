Code Refactoring Training
=========================

Day1 (9:30~12:00) and (1:30~5:00)
---------------------------------

Discuss the question your company encounter when code refactor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. 软件腐烂
#. Why code became bad?
	- It might began with something good
	- But after several versions, it becomes bad
	- Original functionality becomes hiden
#. 案例分析
	+ 故障管理
		- 交付压力 vs 质量 矛盾
	+ 诺基亚
#. 破窗效应 (Broken windows theory)
	- 破窗效应
	- 惯性定律
	
#. 技术债务 (Technical Debt)

#. 重构概念
	
#. Baby Steps
#. 重构-技术难题
	+ 如何发现重构点
	+ 知道重构的目标(结果)
	+ 如何去重构--重构实践
	+ 如何保障重构的正确性--单元测试
#. 识别代码坏味道
#. 时间
	+ 代码时间 1
	+ UT时间 1
	+ 重构时间 1

Day2 (9:30~12:00) and (1:30~5:00)
---------------------------------

#. 代码坏味道列表
#. 表驱动法
	- 直接访问 directory access
	- 索引访问 Index access
	- 阶梯访问 stair-step access

#. 重构到架构
#. Why can save agile
	- You can't stay agile without clean code
	- You can't have clean code without refactoring
	- You can't refactor without good automated success
#. Primitive Obsession (基本型别偏执)
#. 修改遗留代码的艺术-
	+ 改动越少越好(面积)
	+ 可测试性
	+ 可读性
	+ 可扩展性
	+ 服用性
#. Tangling (缠绕)： 把 Base 和 Extension
#. 混乱的原因-开发者技能
#. 修改遗留代码的方法
	+ 新生方法 Sprout Method
	+ 新生类 Sprout Class
	+ 外覆方法 Wrapper Method
	+ 外覆类 Wrapper Class
#. 防止退化
	+ 改进之前，先要防止退化。
	+ 找痛点
		- 复杂
		- 调用频度

学习心得体会
----------

::
 
 通过本次培训，系统性的学习了代码重构的相关知识:
 	1. 为什么要重构 - 软件代码腐烂， 破窗效应 和 技术债务
 	2. 什么是重构
 	3. 代码的坏味道， 以及如何检测代码坏味道， 人工代码评审 和 静态分析工具
 	4. 重构工具 和 重构技巧
 	5. 重构， clean code 和 单元测试的关系
 	6. 重构的流程：Baby Step
 
 重构是一个持续的不间断的过程， 



	
