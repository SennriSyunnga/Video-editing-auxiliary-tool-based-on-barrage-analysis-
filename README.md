# Video-editing-auxiliary-tool-based-on-barrage-analysis-
    原理是这样子的： 假设观众的弹幕是大众趣味的正确反馈，在精彩时刻就会有大量特定弹幕， 
    那么可以反向通过统计一段时间内特定弹幕的数量，来识别出一个长视频中受欢迎的部分。 
    统计是通过输入关键词来进行的，例如对于特别有趣的片段，观众倾向于发送“草”这一弹幕。 
    假设在一段时间内，草的弹幕超出了预设的限制（limit），工具应当记下该时间轴，并提供给剪辑者一个参考时间轴。 
    在一段时间内，由于网络延迟的问题，弹幕的出现不是同步的， 
    观众见证一个亮点时刻时，作为反应的弹幕也会分散在数秒之中。 
    因此将统计的范围放到当前时刻开始的5秒之内。只要总计的弹幕达到了阈值（limit） 就记下当前时刻，
    并且从20秒间隔（interval）后重新开始新一轮判定。
    若当前时刻并不达标，将当前时间往后推进1秒。 之所以设置了20秒的冷却间隔（interval），
    是为了减少重复记轴—— 精彩镜头从来不是瞬间，而是从某个时间点开始的时间段 
    如果不设置冷却时间，那么相邻的数秒都会被纳入统计。 
    这样输出的数个结果的参考意义是很有限的。 
    统计开始容易，统计结束位置很难，但是结束位置可以人为判断，未必要越厨代庖。 
    因此这个工具旨在提供一个“精彩片段的开始大致时间”， 
    给剪辑者、补长视频的观众作为跳转参考。 
    这样一来工具的运行时间也能一定程度上减少。
    
    工具特性：
    1、搜索对象不区分大小写，输入和输出文件名可以自己添加执行路径，如'D:\KaguraMea\video\1.xml'。若不加路径，则默认在同级文件夹内。文件后缀名可省略，将分别强制转.xml和.txt。
    2、如不定义输出文件的名字，则输出和输入文件同名的txt文件。
    3、根据弹幕池的浓度，可以自行调整limit的大小，越浓limit可以设得越高。如果没有得到搜索结果，请勾选仅作弹幕定位来确认弹幕池中是否有所选弹幕。若有，请降低limit，以达到满意的效果。
    
    使用方法：
    1、使用GUI来运行该工具
    这个应该不需要介绍。
	下载链接参考：https://www.bilibili.com/read/cv6140515
	里面有更为详细的GUI介绍。
    2、在终端（Terminal）中运行该工具
    调用命令形如:
    read_kksk_from_text.exe -i D:\Ccode\readthekkskfromtxt\readthekkskfromtxt\20190527_220250.xml -o 1.txt -w 草 -l 20
    可选参数有:
    parser.add_option('-i', '--input', dest='xml_file', default='danmu.xml', help='输入文件名，可包含后缀和指定路径')
    parser.add_option('-o', '--output', dest='out_file', default='', help='输出文件名，可包含后缀和指定路径')
    parser.add_option('-w', '--word', dest='target', default = 'kksk', help = '查询关键字')
    parser.add_option('-l', '--limit', dest='limit', default = 14, help = '纳入统计的最小阈值')
    parser.add_option('-v', '--interval', dest='interval', default = 20, help = '统计最小间隔')
    parser.add_option('-g', '--group', dest='group', default = 5, help = '从当前时间轴开始向前读group秒，若达到limit，则将结果记录，并跳过interval秒')
    parser.add_option('-f', '--flag', dest='flag', default = 0, help = '被gui调用时的标志，此时回传时间轴总长度scale和输出轴的秒制时间')
    
    其中，最后两项仅用于和Gui进行交互而使用，不去更改也没关系的。
	
	最后，感谢wpscott提供的代码和思路。学到了很多技巧。
	比如同义词字典，将相似的关键词重新定向。
	虽然还不太理解全角转半角等部分的涵义，未来将学习这部分内容。
	今后大概想实现的就是关键词复选、通过字典进行关键词的模糊识别(也就是大佬写给我的那段)
	用爬虫读取在线的弹幕文件，降低使用门槛(不需要自己持有xml文件)
	之前问了同学的意见，他觉得普通观众是不善于使用合适的关键词进行搜索的
	把无差别弹幕统计分析做出来可能会有点帮助。
	柱状图将放到次级需求上延后实现，目前的想法是在柱顶显示具体时间。
	(毕竟我们和阿b的那个热点图还是有区别的，阿b的热点轴可以直接跳转……而且我之前观察时不是很理解他的设计原理)
	
	因为目前主要任务还是适应手头工作，暂时先搁置更新。
	将在工作稳定后试着融合wpscott提供的代码，以实现更为便利的功能。
	项目一时兴起，兴趣持续一年，工具仅作学习使用，与工作内容无关。