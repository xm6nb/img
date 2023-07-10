import smtplib  # 导入 SMTP 客户端操作库
from email.mime.text import MIMEText  # 导入 MIMEText 类来表示纯文本或 HTML 消息主体
from email.mime.multipart import MIMEMultipart  # 导入 MIMEMultipart 类来表示多部分邮件
from email.mime.application import MIMEApplication  # 导入 MIMEApplication 类来表示二进制附件

def send_email(subject, message, from_email, from_password, to_email, attachments=None):
    """
    发送电子邮件。

    参数：
    subject：邮件主题字符串。
    message：电子邮件正文字符串。
    from_email：发件人邮箱地址。
    from_password：发件人邮箱密码（此密码应该不被公开）。
    to_email：收件人邮箱地址。
    attachments：一个可选的文件名列表，它们会被添加为电子邮件的附件。

    返回：无
    """
    # 创建一个包含 HTML 和文本消息的多部分消息
    msg = MIMEMultipart('alternative')  # 创建包含多个部分的电子邮件消息。使用 “alternative” 类型表示该消息同时包含 HTML 和纯文本版本。
    msg['Subject'] = subject  # 设置消息主题
    msg['From'] = from_email  # 设置发件人邮箱地址
    msg['To'] = to_email  # 设置收件人邮箱地址

    # 添加纯文本和 HTML 版本的消息
    text = message  # 纯文本版本的消息
    html = message  # HTML 版本的消息
    text_part = MIMEText(text, 'plain')  # 创建一个纯文本 MIME 类型的消息部分
    html_part = MIMEText(html, 'html')  # 创建包含 HTML 格式消息的 MIME 类型的消息部分
    msg.attach(text_part)  # 将纯文本消息部分添加到多部分消息中
    msg.attach(html_part)  # 将 HTML 消息部分添加到多部分消息中

    # 添加附件到电子邮件
    if attachments is not None:
        for attachment in attachments:  # 遍历附件列表中的所有文件名
            with open(attachment, 'rb') as f:  # 打开文件并读取二进制内容
                attach_part = MIMEApplication(f.read(), Name=attachment)  # 创建带有名称和二进制内容的 MIMEApplication 对象
                attach_part['Content-Disposition'] = f'attachment; filename="{attachment}"'  # 设置附件的 Content-Disposition 头
                msg.attach(attach_part)  # 将附件添加到多部分消息中

    # 链接到 SMTP 服务器并发送邮件
    with smtplib.SMTP_SSL('smtp.qq.com', 465) as smtp:  # 使用 SSL 协议链接到 Gmail SMTP 服务器，端口为 465。
        smtp.login(from_email, from_password)  # 登录发件人邮箱
        smtp.sendmail(from_email, to_email, msg.as_string())  # 发送邮件，其中 msg.as_string() 将消息部分转换为字符串

if __name__ == '__main__':
    subject = ''
    message = ''
    from_email = ''
    from_password = ''
    to_email = ''
    attachments = []
    send_email(subject,message,from_email,from_password,to_email,attachments)