# 上海大学二维码生成器

通过这个项目，您可以生成一个二维码，扫描后显示包含上海一些高校及其网站链接的页面。

## 部署链接页面

`links.html` 文件已包含了上海高校的链接，并部署在以下地址：
[https://cfpl24.github.io/links.html](https://cfpl24.github.io/links.html)

## 安装依赖

确保您已经安装了所需的 Python 库。运行以下命令安装依赖：
    ```bash
    pip install streamlit qrcode

## 运行应用程序

运行以下命令启动 Streamlit 应用程序：
    ```bash
    streamlit run app.py

## 生成二维码

打开浏览器，访问 Streamlit 应用程序生成的本地地址（通常是 http://localhost:8501）。在页面上，您将看到生成的二维码。用户可以扫描或下载该二维码，并访问托管的 links.html 页面，显示上海的大学及其网站链接。