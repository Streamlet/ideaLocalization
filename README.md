# 当前进度

已完成：
* 主界面菜单栏翻译

# 使用方法

1. 获取语言包。您可以：
    * 直接从 release 列表下载 resource_zh_CN.jar
    * clone 本项目，运行本项目根目录的 build.py 来生成 resource_zh_CN.jar
2. 将语言包复制到 idea 安装目录的 **lib** 目录下，复制到 **lib** 目录下，复制到 **lib** 目录下
3. 重启 idea

## 注意事项
* 取决于不同操作系统，您可能需要将系统的界面语言设置为简体中文（zh-CN）才能生效。
* 本项目目前只针对 idea，对于 jetBrains 的其他产品尚未做适配，理论上可能支持或部分支持，请自行尝试。

# 加入我们
本项目诚邀您的加入，欢迎您贡献自己的力量。

* 您只需原地修改 resources 下的文件即可，可以在空闲的时候修改一个文件、甚至一行
* 本项目谢绝直接的自动翻译，但不介意您个人使用自动翻译进行某种形式的协助，但最终请您进行人工核对
* 本项目遵循软件行业通用的翻译规范，同时对标 Visual Studio 的翻译。请自行体会。下面会罗列一些细则。

## 分支说明
* dev_build_script: 专门修改构建脚本
* dev_readme：专门修改 readme
* original_resources_tracker: 英文资源文件
* dev_translate：翻译

### 合并策略
* dev_build_script 每次修改并测试通过后合入 master
* dev_readme 每次修改稳定后合入 master
* original_resources_tracker 每次更新资源后打 tag，合入 master
* dev_translate 经常性地从 master 合并新的提交
    * 当 dev_translate 稳定后，从 dev_translate 进行发布
    * dev_translate 在发布时必须处于对 master 可 Fast-Forward 状态
    * dev_translate 发布之后 master Fast-Forward 到 dev_translate

## 协作方式
* Fork 版本库，在 dev_translate 上修改，提交 pull request 回来
* 未来时机成熟的话，成立一个 github 上的 oraganization，届时加入

## 翻译规范

* 标点：行文中一般使用中文半角，某些形式文案中可能需要用英文半角符号
    * 需要打开对话框操作的菜单项，使用英文半角的三个点（“...”）表示
    * 菜单项/按钮后的快捷键两侧使用英文半角括号
* 中英文混排：中文和英文之间需要使用一个半角空格进行分隔
* 菜单项/按钮的快捷键：放在文案之后，如“文件(<u>F</u>)”

### 词汇表
| 英文 | 推荐翻译 | ~~不推荐的翻译~~ |
| --- | --- | --- |
| View | 视图 | ~~查看~~ |
| Build | 生成 | ~~构建~~ |
