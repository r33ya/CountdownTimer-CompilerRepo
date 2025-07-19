from setuptools import setup

APP = ['countdown_timer/app.py']
DATA_FILES = ['assets', 'resources/app_icon.icns']
OPTIONS = {
    'argv_emulation': True,
    'packages': ['pygame', 'objc', 'Foundation', 'AppKit'],
    'iconfile': 'resources/app_icon.icns',
    'plist': {
        'NSAppTransportSecurity': {
            'NSAllowsArbitraryLoads': True
        },
        'NSAppleEventsUsageDescription': '我们需要访问你的媒体库来选择铃声。',
        'NSFileSystemUsageDescription': '我们需要访问文件系统，以便读取铃声文件。',
        'NSDocumentsFolderUsageDescription': '我们需要访问你的文档文件夹，以便加载自定义铃声。',
        'NSMusicUsageDescription': '我们需要访问音乐文件夹中的铃声文件。',
        'NSUserNotificationAlertStyle': '我们需要发送通知以提醒你倒计时结束。',
    },
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
