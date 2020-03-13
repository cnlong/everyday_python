import argparse
import configparser
import sys
import zmail
import os


def get_argparse():
    """
    解析命令行参数
    :return:
    """
    parser = argparse.ArgumentParser(description="A email client in terminal")
    parser.add_argument('-s', action='store', dest='subject', required=True, help='specify a subject (must be in quotes '
                                                                                  'if it has sapces)')
    parser.add_argument('-a', action='store', nargs='*', dest='attaches',
                        required=False, help='attach file(s) to the message')
    parser.add_argument('-f', action='store', dest='conf', required=False,
                        help='specify an alternate .emcli.cnf file')
    parser.add_argument('-r', action='store', nargs='*', dest='recipients', required=True,
                        help='recipient who you are sending the email to')
    parser.add_argument('-v', action='version', version='%(prog)s 0.2')
    return parser.parse_args()


def get_meta_from_config(config_file, sec='Default'):
    """
    解析配置文件
    :param config_file:
    :return:
    """
    meta = {}
    configfile = configparser.RawConfigParser()
    configfile.read(config_file)
    configs = configfile.options(sec)
    for i in configs:
        conf = configfile.get(sec, i)
        meta[i] = conf
    return meta


def get_email_content():
    # 从 sys.sdtin读取标准输入获取邮件的正文内容，可以直接管道符输入或者重定向文件
    return sys.stdin.read()


def main():
    # 新建zmail邮件
    mail = dict()
    # 获取命令参数
    parser = get_argparse()
    mail_subject = parser.subject
    mail_conf = parser.conf
    mail_recipients = parser.recipients
    mail_attaches = parser.attaches
    if not os.path.exists(mail_conf):
        raise SystemExit("{0} is not found".format(mail_conf))
    else:
        meta = get_meta_from_config(mail_conf)
    if mail_attaches:
        mail['attachments'] = list()
        for i in mail_attaches:
            if not os.path.exists(i):
                raise SystemExit("{0} is not found".format(i))
            else:
                mail['attachments'].append(i)
    content = get_email_content()
    mail['subject'] = mail_subject
    mail['content_text'] = content
    server = zmail.server(meta['username'], meta['password'])
    server.send_mail(mail_recipients, mail)


if __name__ == '__main__':
    main()
