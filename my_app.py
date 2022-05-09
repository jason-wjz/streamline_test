import streamlit as st      # import 完了之后直接填网页内容
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# 然后打开 cmd  cd C:\Users\王钧挚\Desktop\泰迪智能科技\st_app (当前工作内容)
# 输入 streamlit run my_app.py (你的工作文件)
# 修改的时候, cmd 和网页都不要关, 网页可以实时更新, 点刷新就行 (不行就 rerun)

# ➢ streamlit run your_app.py # 启动运行APP
# ➢ streamlit config show # 显示配置文档
# ➢ streamlit cache clear # 清除缓存

# -------文本组件
st.title(':heart:Streamlit训练(title):heart:'.center(46, '.'))    # 表情用的是 facebook的 emoji代码
st.text('你的streamlit版本是： {st.__version__} (text)'.center(80, '*'))

st.header('>>>>>>💥文本组件(header)')
st.subheader('My name is Jake(subheader)')

st.write('hello(write)')       # write 除了写入文本，还可以写入图片 (功能比 text多)
st.text('''这里是注释（三个\'\'\'）：
作为SRE，我们有很多很多自动化的工具，大部分都是自动运行的，
还有一部分是CLI，我们一直苦于没有一个自己的管理后台网站，受限于前端能力薄弱，开发出来的网页只能说凑活能用，但是不好用
现在我们有了Streamlit这个神奇，可以仅使用Python就开发一个简单的后台管理网站，同时也可以作为我们的内容输出渠道。
简介
官网：https://streamlit.io/
本身streamlit是给做机器学习的人开发的，作为一个实时的数据展示和输出工具，但是自从我们发现它具有一些交互功能
（Form表单，按钮，单选框，复选框）等功能后，我们借助这些特性，可以开发一个管理网站。
官方Demo
首先安装库：pip3 install streamlit
运行自带的demo：命令行或者CMD输入：streamlit hello
打开网页即可看到Demo''')

st.markdown(
    '''
    **展示标题**
    巴金三部曲
    - 家
    - 春
    - 秋
    '''
)

st.code('print("hello world")   # code + language , 右边可以复制哦', language='python')        # 展示代码
st.balloons()   # 动态效果：气球
st.snow()       # 动态效果：雪花
st.latex(' y = w*x + b')        # 公式展示

# -------数据组件 st.dataframe 交互式表格, st.table 静态表格
st.header('>>>>>>💥数据组件：\n 1.st.dataframe 交互式表格  2.st.table 静态表格')
data = pd.read_csv('./data/titanic_data.csv')
st.dataframe(data)
# st.table(data)  # 数据量不大的情况下可以用 table, 因为 table是强制展示所有数据内容
st.metric('温度', '23℃', delta='-2℃')     # 计算, delta就是差值
st.metric('温度', '23℃', delta='2℃')     # 计算
# 将两个数字展现在同一行（上面的会分两行展示）
col1, col2 = st.columns(2)  # 分成两列
with col1:  #第一列的东西
    st.metric('温度', '23℃', delta='-2℃')
with col2:  #第二列的东西
    st.metric('温度', '23℃', delta='2℃')

# -------图表组件
st.header('>>>>>>💥图表组件')
data_np = np.random.random((30, 4))
# st.line_chart(data_np)      # 折线图
# st.bar_chart(data_np)       # 条形图
st.area_chart(data_np)      # 填充后的折线图
st.map(pd.DataFrame([[112, 22]], columns=['lon', 'lat']))       # 真实的地图, pd.DataFrame([[经度，维度]], columns=['longitude', 'latitude'])
#fig, [ax1, ax2] = plt.subplots(2)    # 一个 叫 fig 的图表, 有 ax1 和 ax2 两个子图 （subplot输入的)
#ax1.plot(data_np[:, 0])
#ax2.plot(data_np[:, 1])      # 给 ax1 画 data的第一列数据， ax2 画 data的第二列
#ax1.set_title('test')           # 设置图表的 title
#ax2.set_title('train')           # 设置图表的 title
#st.pyplot(fig)                  # 展示

# -------多媒体组件
st.header('>>>>>>💥多媒体组件')
st.subheader('爱心'.center(10, '💘'))
st.image('./Video_pictures_others/aixin.jpg')     # 展示组件  可以输入工作路径, 也可以放网址
st.subheader('七里香-周杰伦'.center(15, '🎶'))
st.audio('./Video_pictures_others/七里香-周杰伦.mp3')

