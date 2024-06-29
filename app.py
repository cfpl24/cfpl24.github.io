import streamlit as st
import qrcode
from PIL import Image
import io

# 中间页面的 URL
redirect_url = "https://cfpl24.github.io/links.html"

# 生成包含redirect_url的二维码
def generate_qr_code(url):
    # 生成二维码
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # 创建二维码图像
    img = qr.make_image(fill='black', back_color='white')
    
    # 将二维码图像保存到内存中的字节流
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    byte_im = buf.getvalue()
    
    return byte_im

# Streamlit 应用程序
st.title("打开手机扫一扫")

# 生成二维码
qr_image = generate_qr_code(redirect_url)

# 将二维码图像显示在网页上
st.image(qr_image, caption='Generated QR Code')

# 提供二维码图像的下载链接
st.download_button(
    label="保存二维码",
    data=qr_image,
    file_name="qrcode.png",
    mime="image/png"
)
